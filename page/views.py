from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.
def home(request):
    designer = Designer.objects.all()
    # home에서 요청이 들어오면 home.html이 실행됨
    return render(request, 'home.html', {'designers' : designer})

def introduce(request):
    return render(request, 'introduce.html')
    
    # urls.py에 "designer_id" 라고 정의했기 때문에 "pk" 대신 "desginer_id"를 적음
def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        # designer라는 객체에 맞춤
        post = Designer()
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id)

def delete(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)
    post.delete()

    return redirect('home')