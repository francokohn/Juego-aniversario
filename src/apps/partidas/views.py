from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from utils.user_test import es_admin
from apps.preguntas.models import Partida, Pregunta, Respuesta
import math
import random

RUTA_INICIO = 'usuarios:inicio'
SESSION_KEY = 'resultado'

@login_required()
def listar(request):
    template_name = "partidas/listar.html"
    user = request.user
    partidas = Partida.objects.all() if es_admin(user) else Partida.objects.filter(usuario_id = user.id)
    
    ctx = {
		'partidas' : partidas
	}

    return render(request, template_name, ctx)

@login_required()
def jugar(request):
    user = request.user

    if request.method == 'POST':
        resultados, puntaje = get_resultado(request.POST)
        user.partida_set.create(puntos = puntaje)

        request.session[SESSION_KEY] = { 
            'resultados': resultados,
            'puntaje': puntaje
        }

        return redirect('partidas:resultado')
    else:
        template_name = "partidas/jugar.html"
        nivel = get_nivel(request.user)
        preguntas = get_preguntas(nivel)
        ctx = { 'preguntas': preguntas }

        return render(request, template_name, ctx)

def resultado(request):
    template_name = "partidas/resultado.html"

    if SESSION_KEY in request.session:
        ctx = request.session[SESSION_KEY]
        del request.session[SESSION_KEY]
        return render(request, template_name, ctx)
    else:
        return redirect(RUTA_INICIO)

def get_nivel(jugador):
    try:
        puntaje_maximo = jugador.partida_set.latest('puntos')
        puntos = puntaje_maximo.puntos
        return math.floor(puntos / 10)
    except Partida.DoesNotExist:
        return 0

def get_preguntas(nivel):    
    ids = [i.id for i in Pregunta.objects.filter(nivel = nivel)]
    random.shuffle(ids)
    return [Pregunta.objects.get(id=i) for i in ids[:10]]

def get_resultado(request):
    puntaje = 0
    resultados = list()
    for key, value in request.items():
        if 'pta-' in key:
            rta = Respuesta.objects.get(pk = value)
            id_pta = key.split('-')[1]
            pta = Pregunta.objects.get(pk = id_pta)

            if (rta.es_correcta):
                resultados.append((pta.texto_pregunta, rta.texto_respuesta, True))
                puntaje += pta.nivel + 1
            else:
                resultados.append((pta.texto_pregunta, rta.texto_respuesta, False))

    return (resultados, puntaje)