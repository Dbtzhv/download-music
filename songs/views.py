from rest_framework.views import APIView
from rest_framework.response import Response
from songs.models import Song
from songs.serializers import SongSerializer
from rest_framework.reverse import reverse
from django.http import FileResponse
from django.views import View
from users.models import User
from rest_framework import status


class SongView(APIView):
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data['user_id']
        token = serializer.validated_data['token']
        song_mp3 = serializer.validated_data['song_mp3']

        user = User.objects.filter(user_id=user_id)

        if not user:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        elif user.exists() and user.last().token!=token:
            return Response("Incorrect token", status=status.HTTP_403_FORBIDDEN)

        song = Song.objects.create(song_mp3=song_mp3, user_id=user_id, token=token)

        download_url = reverse('record-download') + f'?id={song.song_id}&user={user_id}'

        response_data = {
            'download_url': request.build_absolute_uri(download_url)
        }

        return Response(response_data)


class SongDownloadView(View):
    def get(self, request):
        song_id = request.GET.get('id')
        user_id = request.GET.get('user')

        # Получите запись по song_id и user_id
        song = Song.objects.get(song_id=song_id, user_id=user_id)

        # Откройте файл и верните его в качестве ответа
        file_path = song.song_mp3.path
        file_name = song.song_mp3.name
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
