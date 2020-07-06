from django.http import HttpResponse
from django.shortcuts import render
import json
from . import modifjson
from django.template.loader import render_to_string
from django.shortcuts import render

with open("C:/Users/julien/Documents/dentiste/pageweb/pageApps/static/pageApps/40623553813XP.json","r") as j:
  data = json.load(j)

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'pageApps/accueil.html')

def view_client(request, id_client):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)

    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_client)    
    ) 
    """
    return render(request, 'pageApps/client.html', {'id_client': id_client})

def my_view(request):
    as_file = request.GET.get('as_file')
    njson = modifjson.modif_json(data)
    context = {'body': njson}
    
    return render(request, 'pageApps/templateTooths.html', context=context)

