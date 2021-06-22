from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def empty(request):
    return redirect("/shows") #redirecciona la ruta vacía al index (template principal)


def index(request):
    context={
        "tvShows":Show.objects.all()
    }
    return render(request, "index.html", context)


def addShowTemp(request):
    return render(request, "newshow.html") # solo nuestra el template para ingresar un nuevo show

def addShow(request):
    print(request.POST)
    title=request.POST["title"]
    network=request.POST["network"]
    release=request.POST["release"]
    descr=request.POST["description"] #recibo los datos del formulario
    Show.objects.create(title=title, network=network, release_date=release, description=descr)
    newShowAdded=Show.objects.last() #recupero el ultimo objeto creado
    newShowId=newShowAdded.id  #obtengo su id
    return redirect(f"create/{newShowId}") # redirijo con el id

def showCreated(request, id):
    tvShow=Show.objects.get(id=id)
    context={
        "id":id,
        "title":tvShow.title,
        "network":tvShow.network,
        "release":tvShow.release_date,
        "description":tvShow.description,
        "updated":tvShow.updated_at
    }
    return render(request, "oneshow.html", context)


def editShow(request, id):
    showToEdit=Show.objects.get(id=id)
    context={
        "id":id,
        "title":showToEdit.title,
        "network":showToEdit.network,
        "release":showToEdit.release_date,
        "description":showToEdit.description      
    }
    return render(request, "editshow.html", context)


def update(request, id):
    showToUpdate=Show.objects.get(id=id)
    showToUpdate.title=request.POST["title"]
    showToUpdate.network=request.POST["network"]
    showToUpdate.release=request.POST["release"]
    showToUpdate.description=request.POST["description"]
    showToUpdate.save()
    messages.success(request, "The Show has been Updated")

    return redirect(f"/shows/{id}/edit")


def destroy(request, id):
    showToDelete=Show.objects.get(id=id)   
    showToDelete.delete()
    messages.success(request, "The Show has been Deleted")
    return redirect("/shows")
