from django.shortcuts import render, redirect 
# Create your views here.

# 
from django.contrib.auth.forms import (
  AuthenticationForm, 
  UserCreationForm, 
  PasswordChangeForm,  
)
# 
# from .models import User

# 로그인, 로그아웃 기능 사용 
from django.contrib.auth import login as auth_login, logout as auth_logout 
# 
from .models import User

# login decorator ->  로그인한 사용자만 쓸 수 있는 기능 정의 
from django.contrib.auth.decorators import login_required

# 
from .forms import CustomUserCreationForm, CustomUserChangeForm

#
from django.contrib.auth import update_session_auth_hash

def index(request): 
    persons = User.objects.all()
    context = {
        'persons' : persons
    }
    return render(request, 'accounts/index.html', context)

def login(request): 
    if request.method == 'POST': # 로그인 버튼 눌렀을 때 
        form = AuthenticationForm(request, request.POST) # AuthenticationForm 의 첫 번째 인자 : request 
        # request.POST : 사용자가 입력한 ID, Password 
        # request : HTTP 요청 전체 
        if form.is_valid(): 
            auth_login(request, form.get_user())
            return redirect('articles:index') # 로그인 완료하면 메인 페이지로 

    else: # 로그인 버튼 누르기 전 
        form = AuthenticationForm() # 빈 폼 
    context = { 
        'form' : form 
    }
    return render(request, 'accounts/login.html', context)

@login_required # 로그인한 사용자만 사용할 수 있게 하는 기능   
def logout(request): 
    auth_logout(request) 
    return redirect('articles:index')
 
def signup(request): 
    # is_authenticated : 이미 인증된 사용자라면 
    if request.user.is_authenticated: 
        return redirect('articles:index') 
    
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save()
            auth_login(request, user) 
            return redirect('articles:index')
    else: 
        form = CustomUserCreationForm()
    context = {
        'form' : form , 
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request): 
    request.user.delete()
    # request.user : request에 포함되어 있는 user 정보 (현재 로그인되어있는) 
    return render('articles:index')

@login_required
def update(request): 
    if request.method == 'POST': 
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid(): 
            form.save()
            return redirect('articles:index') 
    else: # 회원 정보 버튼 누르기 전 
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/update.html', context) 
    

@login_required
def change_password(request, user_pk): 
    if request.method == 'POST': 
        form = PasswordChangeForm(request.user, request.POST) # 첫 번째 인자는 user, 두 번째 인자는 데이터 
        if form.is_valid(): 
            form.save() 
            # 세션 무효화 방지 과정 (자동 로그아웃 방지)
            # hash 함수로 현재 사용자의 인증 세션 갱신 
            update_session_auth_hash(request, user) 
            return redirect('articles:index')
    else: 
        form = PasswordChangeForm(request.user) 
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/change_password.html', context) 
