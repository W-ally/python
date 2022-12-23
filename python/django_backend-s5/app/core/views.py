

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

import datetime
from .serializers import UserSerializer
from .models import User
from .tasks import unsync_notify

import jwt

class StatusView(APIView):
  
   def get(self, request):
       return Response({'result':'server is running and OK'}, status=status.HTTP_200_OK)

class UserViewSet(ModelViewSet):
    
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    # def retrieve(self, request, *args, **kwargs):

    #     params = kwargs
    #     name = params['pk']
    #     print(params)

    #     users = User.objects.filter(name__icontains=name)
    #     serializer = UserSerializer(users, many=True)

    #     return Response(serializer.data)


class RegisterView(APIView):

    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        name = request.data['name']
        unsync_notify.apply_async(args=[name])

        return Response(serializer.data)

class LoginView(APIView):

    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id': user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt':token
        }

        return response

class UserView(APIView):

    def get(self, request):
        
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
    
        return Response(serializer.data)
    
class LogoutView(APIView):

    def post(self, request):
        
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'sucess logout'
        }

        return response
