from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Persona
import requests

def persona_list(request):
    personas = Persona.objects.all().order_by('-id')
    context = {
        'personas':personas
    }
    print(context)
    return render(request, 'persona_app/persona_list.html', context)

def persona_details(request, id):
    persona = Persona.objects.get(id=id)
    context = {
        'persona':persona
    }
    print(context)
    return render(request, 'persona_app/persona_details.html', context)

def persona_generate(request):
    result = requests.get('https://randomuser.me/api?nat=fr')
    json_result = result.json()
    importedPersona = Persona(first_name=json_result['results'][0]['name']['first'],
        last_name       = json_result['results'][0]['name']['last'],
        address_street  = json_result['results'][0]['location']['street']['name'],
        address_number  = json_result['results'][0]['location']['street']['number'],
        city            = json_result['results'][0]['location']['city'],
        postcode        = json_result['results'][0]['location']['postcode'],
        country         = json_result['results'][0]['location']['country'],
        email           = json_result['results'][0]['email'],
        username        = json_result['results'][0]['login']['username'],
        password        = json_result['results'][0]['login']['password'],
        age             = json_result['results'][0]['dob']['age'],
        picture         = json_result['results'][0]['picture']['large'])
    importedPersona.save()
    return redirect('url_persona_details',id=importedPersona.id)
