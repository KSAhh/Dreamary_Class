from django.shortcuts import render

# Create your views here.
def home(request):
    # home에서 요청이 들어오면 home.html이 실행됨
    return render(request, 'home.html')

def introduce(request):
    return render(request, 'introduce.html')
    