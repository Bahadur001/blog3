from django.shortcuts import render
from .models import Article
# Create your views here.
def home__view(request):
    return render(request, 'index.html')
 
def my__blogs__view(request):
    articles = Article.objects.all()
    return render(request, 'my-blogs.html', {'articles': articles})
 
def our__blogs__view(request):
    articles = Article.objects.all()
    return render(request, 'our-blogs.html', {'articles': articles})
 

 
def about__view(request):
    return render(request, 'about.html')


def contact__view(request):
    return render(request, 'contact.html')