from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer


User = get_user_model()


class RegisterView(GenericAPIView):
    """
    User register view
    """

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    """
    User login view
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(
            serializer.error_messages, status=status.status.HTTP_401_UNAUTHORIZED
        )
