from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from helpers.email import validateUser, recoveryPassword

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models import Error

import random
import string

User = get_user_model()

# Create your views here.
def temporal():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

class UserAccountCreateView(APIView):

    def post(self, request):
        try:
            email = request.data.get('email')
            username = request.data.get('username')
            password = temporal()
            tokenValidation = temporal()
            user = User.objects.filter(email=email).first()

            if user:
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.create_user(username=username, email=email, password=password, tokenValidation=tokenValidation)
                data = {
                    'username': username,
                    'email': email,
                    'password': password,
                    'tokenValidation': tokenValidation
                }
                validateUser(data)
                return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class ValidateUserAccountView(APIView):
    def post(self, request):
        try:
            tokenValidation = request.data.get('tokenValidation')
            user = User.objects.filter(tokenValidation=tokenValidation).first()

            if user:
                user.is_active = True
                user.tokenValidation = None
                user.save()
                return Response({'success': 'User validated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RecoveryUserPassword(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            user = User.objects.filter(email=email).first()

            if user and user.is_active:
                user.recuperationCode = temporal()
                user.save()
                data = {
                    'email': email,
                    'recuperationCode': user.recuperationCode
                }
                recoveryPassword(data)
                return Response({'success': 'Email sent successfully'}, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RecoverUserPasswordValidate(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            repeatPassword = request.data.get('repeatPassword')
            recuperationCode = request.data.get('recuperationCode')
            user = User.objects.filter(email=email, recuperationCode=recuperationCode).first()
            
            if user and user.is_active:
                if password == repeatPassword:
                    user.set_password(password)
                    user.recuperationCode = None
                    user.save()
                    return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UserAccountLoginView(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                Token.objects.filter(user=user).delete()
                token, _ = Token.objects.get_or_create(user=user)

                return Response({'success': 'User logged in successfully', 'token': token.key}, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UserAccountLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            logout(request)
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response({'success': 'User logged out successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class FirstLoginChangePasswordView(APIView):
    def post(self, request):
        try:
            user = request.user
            password = request.data.get('password')
            repeatPassword = request.data.get('repeatPassword')
            
            if user and user.is_active:
                if password == repeatPassword:
                    user.set_password(password)
                    user.first_login = False
                    user.save()
                    return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = Error.objects.create(error=e)
            error.save()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        