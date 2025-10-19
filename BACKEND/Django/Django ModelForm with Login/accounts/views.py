from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST

# Create your views here.

def signup(request):
    # 로그인 되어 있으면, 목록페이지로 이동
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        # UserCreationForm => models.ModelForm (User 객체 생성)
        # 값을 받아서
        form = UserCreationForm(request.POST)
        # 검증하고(Common...Length....)
        if form.is_valid():
            # 저장한다.
            user = form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        # 데이터를 받아와서 => 아이디/비밀번호 일치 => 로그인(세션 생성) => redirect
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')