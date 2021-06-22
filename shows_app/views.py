from django.shortcuts import render, redirect
from .models import Show, Network
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
    context={
        "allNetworks":Network.objects.all()   
    }    
    return render(request, "newshow.html", context) # solo nuestra el template para ingresar un nuevo show

def addShow(request):    
    title=request.POST["title"]
    network=request.POST["network"]
    release=request.POST["release"]
    descr=request.POST["description"] #recibo los datos del formulario
    objetoNetwork=Network.objects.get(id=network) #traigo el objeto network con el id que lega en el post
    Show.objects.create(title=title, network=objetoNetwork, release_date=release, description=descr)     
    newShowAdded=Show.objects.last() #recupero el ultimo objeto creado   
    newShowId=newShowAdded.id  #obtengo su id
    return redirect(f"create/{newShowId}") # redirijo con el id


def showCreated(request, id):
    tvShow=Show.objects.get(id=id)
    context={
        "id":id,
        "title":tvShow.title,
        "network":tvShow.network.name,
        "release":tvShow.release_date,
        "description":tvShow.description,
        "updated":tvShow.updated_at
        
    }
    return render(request, "oneshow.html", context)


def editShow(request, id):
    showToEdit=Show.objects.get(id=id)
    netw=Network.objects.get(id=showToEdit.network.id)#traigo el objeto por el id
    context={
        "id":id,
        "title":showToEdit.title,
        "network":netw, #mando el objeto
        "release":showToEdit.release_date,
        "description":showToEdit.description,
        "allNetworks":Network.objects.all()       
    }
    return render(request, "editshow.html", context)


def update(request, id):
    showToUpdate=Show.objects.get(id=id)#traigo el show por su id y lo guardo
    showToUpdate.title=request.POST["title"]#guardo lo que viene del post en el campo correspondiente
    netwId=request.POST["network"]#capturo el id de la network
    objectNetwork=Network.objects.get(id=netwId)#con el id traigo el objeto
    showToUpdate.network=objectNetwork #asigno el objeto al campo (de la relacion)
    showToUpdate.release=request.POST["release"]
    showToUpdate.description=request.POST["description"]
    showToUpdate.save() #guardo y actualizo
    messages.success(request, "The Show has been Updated")

    return redirect(f"/shows/{id}/edit") #redirecciono a la pagina edit


def destroy(request, id):
    showToDelete=Show.objects.get(id=id)   
    showToDelete.delete()
    messages.success(request, "The Show has been Deleted")
    return redirect("/shows")
