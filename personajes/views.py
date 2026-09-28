from django.shortcuts import render
import requests

URL_API = 'https://potterapi-fedeperin.vercel.app/es/characters'


def lista_personajes(request):
    respuesta = requests.get(URL_API)
    personajes = respuesta.json()

    return render(request, 'personajes/lista.html', {
        'personajes': personajes
    })


def detalle_personaje(request, indice):
    respuesta = requests.get(URL_API)
    personajes = respuesta.json()

    personaje = personajes[indice]

    return render(request, 'personajes/detalle.html', {
        'personaje': personaje
    })

