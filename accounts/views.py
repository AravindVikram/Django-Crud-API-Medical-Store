from rest_framework.views import APIView
from .serializers import  UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



#Register
class RegisterAPI(APIView):
   
   def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return  Response({'User Registered Succesfully': serializer.data['username']})
        else:
         return Response({'errors':serializer.errors}, status=400)
        

#LOGIN
class LoginAPI(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
                          
        user = authenticate(username=username, password=password)

        if user is not None:
            token_obj , _ = Token.objects.get_or_create(user=user)  
            
            return  Response({ 'token':str(token_obj), 
                              'message' : 'You have Succesfully logged in and token has been generated'},status=200 )
            
        return Response({'error': 'Invalid credentials'}, status=401)
    

class LogoutAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete() #deletes the authentication token associated with the currently authenticated user.
        return Response({'message': 'User has been logged out.'})
