from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm 

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user) #get_user 바로 써도 됨
            return redirect('articles:index')
    else:
        form = AuthenticationForm(request)
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 로그인화면 유지하는 방법 두가지임 이거말고 딴건 auth
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    # 로그인 된 사용자만 가능한 요청이므로
    # request.user 가 요청한 사용자의 인스턴스 
    
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')