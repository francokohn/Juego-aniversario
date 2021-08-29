from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from utils.user_test import es_admin
from apps.preguntas.models import Partida

@login_required()
def listar(request):
    template_name = "partidas/listar.html"
    user = request.user
    partidas = Partida.objects.all() if es_admin(user) else Partida.objects.filter(pk = user.id)
    
    ctx = {
		'partidas' : partidas
	}

    return render(request, template_name, ctx)


def jugar(request):
    template_name = "partidas/jugar.html"
    return render(request, template_name, {})
