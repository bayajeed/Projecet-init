from django.shortcuts import render, redirect
from users.models import CustomUser
from Ecom.views import base
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.hashers import check_password # type: ignore

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer

from rest_framework.authtoken.views import ObtainAuthToken # login with token

#from django.http import HttpResponse
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Get the username from the form
        password = request.POST.get('password') # Get the password from the form
        # user = CustomUser.objects.get(username=username) # Get the user with the username
        try:
            user = CustomUser.objects.get(username=username) # Get the user with the username
        except:
            context = {'message': 'User does not exist'}
            return render(request, 'signin.html', context)
            #return render(request, 'signin.html', {'message': 'User does not exist'})
        if check_password(password, user.password):
            login(request, user)
            return redirect('base') # Redirect to the base page
        context = {'message': 'Invalid Password'}
        # nicher code run dile password check kore na
        # if user is not None:
        #     login(request, user)
        #     return redirect('base') # Redirect to the base page
        return render(request, 'signin.html', context)
    return render(request, 'signin.html')

# kaj koyna..............
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password == password2:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name) # Create a new user
            user.save()
            return redirect(signin) # Redirect to the login page
            #return HttpResponse('User created successfully')
        #user = CustomUser.objects.create_user(username=username, password=password, email=email) # Create a new user
        #print(username, email, first_name, last_name, password, password2) # print hoyna keno?
        # user.save() # Save the user
        #return redirect('login') # Redirect to the login page
    return render(request, 'signup.html')


# for API for All GET POST PUT PATCH
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    #serializer_class = UserSerializer(queryset, many = True) # queryset kno dilam, # karon serializer class e queryset pass korte hoy
    
# login with token
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        check_user = CustomUser.objects.filter(username=username).first()
        if not check_user:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        response = super().post(request, *args, **kwargs)
        token = response.data['token']
        user = CustomUser.objects.get(username=username)
        usersirializer = UserSerializer(user)
        return Response({
            'token': token,
            'user': usersirializer.data
        }, status=status.HTTP_200_OK)
