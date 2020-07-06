import json
from modifjson import modif_json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pageweb.settings')
from django.core.management import execute_from_command_line
from django.template.loader import render_to_string
from django.shortcuts import render
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'pageweb.settings'

with open("C:/Users/julien/Documents/dentiste/pageweb/pageApps/static/pageApps/40623553813XP.json","r") as j:
  data = json.load(j)

def my_view(request):
    as_file = request.GET.get('as_file')
    njson = modif_json(data)
    body = ""
    for i in range(len(njson)) :
        if njson[i]['type'] == "anatomy" :
            body += "<ul> "+ njson[i]['subType'] + "</ul> "
            
    context = {'body': body}
    
    if as_file:
        content = render_to_string('templateTooths.html', context)                
        with open('C:/Users/julien/Documents/dentiste/pageweb/python/templateTooths.html', 'w') as static_file:
           static_file.write(content)

    return render('templateTooths.html', context)

        