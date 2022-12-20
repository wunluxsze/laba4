from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from .models import *

def index(request):
    films = Films.objects.all()
    return render(request,"index.html",{'films':films})

def create(request):
    categories()
    if request.method == "POST":
        films = Films()
        films.title = request.POST.get("title")
        films.date = request.POST.get("date")
        films.actors = request.POST.get("actors")
        films.dateView = request.POST.get("dateView")
        films.genre_id = request.POST.get("category")
        films.save()
        return redirect("home")

    categori = Category.objects.all()
    return render(request,"create.html",{"categori":categori})

def edit(request,id):
    try:
        film = Films.objects.get(id = id)
        if request.method == "POST":
            film = Films.objects.get(id = id)
            film.title = request.POST.get("title")
            film.date = request.POST.get("date")
            film.actors = request.POST.get("actors")
            film.dateView = request.POST.get("dateView")
            film.genre_id = request.POST.get("category")
            film.save()
            return redirect("home")
        else:
            categori = Category.objects.all()
            return render(request, "edit.html", {"categori":categori,"films":film})
    except Films.DoesNotExist:
        return HttpResponseNotFound("<h2>Фильм не найден</h2>")

def delete(request,id):
    try:
        films = Films.objects.get(id = id)
        films.delete()
        return redirect("home")
    except Films.DoesNotExist:
        return HttpResponseNotFound("<h2>Фильм не найде</h2>")

def categories():
    if Category.objects.all().count() == 0:
        Category.objects.create(title = "Романтика")
        Category.objects.create(title = "Боевик")
        Category.objects.create(title = "Драма")
        Category.objects.create(title = "Ужасы")
        Category.objects.create(title = "Приключение")
