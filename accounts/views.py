from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    # 리퀘스트 메소드가 post일 땐
    # DB에 저장한다
    if request.method == "POST":
        forms = SignupForm(request.POST)
        # 유효성 검사 진행 후 DB에 저장
        if forms.is_valid():
            forms.save()
            return render(request, "base.html")
    
    # 리퀘스트 메서드가 get 또는 유효성 검사를 통과하지 못했다면,
    else:
        forms = SignupForm()
    
    context = {
        "forms" : forms,
    }
    return render(request, "accounts/signup.html", context)

def login(request):
    # request method가 POST일 때
    if request.method == "POST":
        # 사용자의 입력값을 받는다.
        # 모델폼을 상속하는 폼이 아니기 때문에 요구하는 문법(매개변수)가 다르다.
        forms = AuthenticationForm(request, data=request.POST)
        # 유효성 검사를 통과하면 세션에 저장한다.(내장함수 login으로)
        if forms.is_valid():
            auth_login(request, forms.get_user())
            # 성공하면 base.html로 보낸다(아직 구현된 템플릿이 적으니까)
            return render(request, "base.html")
    
    # request method가 GET 혹은 유효성 검사 실패한 사용자의 입력값이라면
    else:
        # 빈 폼 혹은 오류 메시지를 출력하는 폼
        forms = AuthenticationForm()
        
    context = {
        "forms" : forms,
    }
    return render(request, "accounts/login.html", context)

def index(request):
    # 회원 정보를 가지고 있는 유저 객체
    infos = get_user_model().objects.all()
    context = {
        "infos" : infos,
    }
    
    # 유저객체에 대한 정보를 템플릿에 출력한다.
    return render(request, "accounts/index.html", context)