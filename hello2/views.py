from django.shortcuts import render

def hello2_view(request):
    return render(request, 'hello2/home.html')

# Create your views here.
