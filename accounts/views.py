from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import SignupForm
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