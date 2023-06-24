from django.contrib.auth import authenticate, login, logout
from rest_framework import status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.common.utils.app_functions import get_tokens_for_user
from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserSerializer, RightSerializer, \
    RoleSerializer, UserRoleSerializer
from ..models import User, Right, UserRole, Role


class RightViewSet(ModelViewSet):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    http_method_names = ['post', 'patch', 'get', 'put', 'delete']


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    http_method_names = ['post', 'patch', 'get', 'put', 'delete']


class UserRoleViewSet(ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    http_method_names = ['post', 'patch', 'get', 'put', 'delete']


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]

    # authentication_classes = []

    @staticmethod
    def is_authenticated(request):
        if not bool(request.user and request.user.is_authenticated):
            raise exceptions.AuthenticationFailed()

    @action(detail=False, methods=['post'], url_name='reset-password', url_path='reset-password')
    def reset_password(self, request):
        self.is_authenticated(request)
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)  # Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'], url_name='register', url_path='register')
    def register_user(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_name='login', url_path='login')
    def login_user(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'message': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            user = UserSerializer(user)
            return Response({'message': 'Login Success', 'user': user.data, **auth_data},
                            status=status.HTTP_200_OK)
        raise exceptions.NotAuthenticated()

    @action(detail=False, methods=['post'], url_name='token-refresh2', url_path='token-refresh2')
    def token_refresh(self, request):
        """"Refresh token should be sent in this method"""
        # jwt.decode(
        #     token,
        #     SIMPLE_JWT['SIGNING_KEY'],
        #     algorithms=[SIMPLE_JWT['ALGORITHM']],
        # )
        # jwt_authenticator = JWTAuthentication()
        # response = jwt_authenticator.authenticate(request)
        # if response is not None:
        #     user, token = response
        #     return Response(data={
        #         "this is decoded token claims", token.payload
        #     }, status=status.HTTP_200_OK)
        # else:
        #     return Response({
        #         'error': 'Bad Request (400)'
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # get_refreshed_tokens()
        ...

    @action(detail=False, methods=['post'], url_name='logout', url_path='logout')
    def logout_user(self, request):
        logout(request)
        return Response({'message': 'Successfully Logged out'}, status=status.HTTP_200_OK)
