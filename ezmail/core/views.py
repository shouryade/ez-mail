from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


@api_view(["GET"])
def get_users(request):
    """
    Get all users
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"users": serializer.data})


@api_view(["POST"])
def create_user(request):
    """
    Create a new user
    """
    username = request.data.get("username")
    email = request.data.get("email")
    phone = request.data.get("phone")
    user = User.objects.create(username=username, email=email, phone=phone)
    serializer = UserSerializer(user)
    return Response({"user": serializer.data})
