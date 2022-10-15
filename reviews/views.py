from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Review
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create(request):
    if request.method == "POST":
        
        forms = PostForm(request.POST)
        # 사용자가 입력한 값이 유효성을 통과하면 DB에 저장한다.
        if forms.is_valid():
            forms.save()
            # 게시글 작성 후 제대로 작성됐는지 확인하도록 게시글 상세보기 페이지로 보낸다.
            # return redirect(request, "reviews/detail.html", Review.objects.all()[0].pk)
            return redirect('reviews:index') 
    # request.method 가 GET일 경우
    else:
        # 빈 폼
        forms = PostForm()
    context = {
        "forms" : forms,
    }
    return render(request, "reviews/create.html", context)

def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews" : reviews,
    }
    return render(request, "reviews/index.html", context)