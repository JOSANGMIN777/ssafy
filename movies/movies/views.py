from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    return render(request, 'movies/create.html')

def new(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Movie(title=title, content=content)
    article.save()
    return redirect('movies:index')