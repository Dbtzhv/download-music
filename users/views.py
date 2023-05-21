from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']

        user = User.objects.create(name=name)

        response_data = {
            'token': user.token,
            'user_id': user.user_id,
        }

        return Response(response_data)
