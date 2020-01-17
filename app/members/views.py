import requests
from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm

User = get_user_model()


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('books:book-list')
    else:
        form = LoginForm()

    login_base_url = 'http://nid.naver.com/oauth2.0/authorize'
    login_params = {
        'response_type': 'code',
        'client_id': 'wJcJbLrIqZv3Nq83VgKZ',
        'redirect_uri': "http://localhost:8000/members/naver-login/",
        'state': 'RANDOM_STATE',
    }
    login_url = '{base}?{params}'.format(
        base=login_base_url,
        params='&'.join([f'{key}={value}' for key, value in login_params.items()])
    )
    print(login_url)

    context = {
        'form': form,
        'login_url': login_url,
    }
    #return HttpResponse('hello')
    return render(request, 'members/login.html', context)


def signup_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:book-list')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    # return HttpResponse('hello')
    return render(request, 'members/signup.html', context)


def logout_view(request):

    logout(request)
    return redirect('members:login')


def naver_login(request):

    code = request.GET.get('code')
    state = request.GET.get('state')
    if not code or not state:
        return HttpResponse('code 또는 state가 전달되지 않았습니다.')

    token_base_url = 'https://nid.naver.com/oauth2.0/token'
    token_params = {
        'grant_type': 'authorization_code',
        'client_id': 'wJcJbLrIqZv3Nq83VgKZ',
        'client_secret':'hk2BMmOfeG',
        'code': code,
        'state': state,
        'redirectURI' : 'http://localhost:8000/members/naver-login/',
    }

    token_url = '{base}?{params}'.format(
        base=token_base_url,
        params='&'.join([f'{key}={value}' for key, value in token_params.items()])
    )
    response = requests.get(token_url)
    access_token = response.json()['access_token']
    print(access_token)

    me_url= 'https://openapi.naver.com/v1/nid/me'
    me_headers = {
        'Authorization': f'Bearer {access_token}',
    }
    me_response = requests.get(me_url, headers=me_headers)
    me_response_data = me_response.json()
    print(me_response_data)

    unique_id = me_response_data['response']['id']
    print(unique_id)

    naver_username = f'n_{unique_id}'
    if not User.objects.filter(username=naver_username).exists():
        user = User.objects.create_user(username=naver_username)
        login(request, user)
    return redirect('members:login')


