from django.shortcuts import render, redirect
from .models import Pregunta
from .forms import PreguntaForm, RespuestaForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from utils.user_test import es_admin

@login_required()
@user_passes_test(es_admin, login_url = '', redirect_field_name = None)
def listar(request):
    template_name = "preguntas/listar.html"
    preguntas = Pregunta.objects.all()

    ctx = {
        'preguntas' : preguntas
    }    

    return render(request, template_name, ctx)

@login_required
@user_passes_test(es_admin, login_url = '/preguntas/', redirect_field_name = None)
def crear(request):
    template_name = "preguntas/crear.html"

    ctx = { 
        'form': PreguntaForm(),
        'completo': False,
        'tipo': 'incorrecta'
    }

    if request.method == "POST":
        ctx['form'] = RespuestaForm()

        if 'pregunta' not in request.session:
            request.session['pregunta'] = request.POST
            ctx['tipo'] = 'correcta'
        elif 'respuesta_correcta' not in request.session:
            request.session['respuesta_correcta'] = request.POST
        elif 'respuestas_incorrectas' not in request.session:
            request.session['respuestas_incorrectas'] = [request.POST]
            ctx['completo'] = True
        else:
            request.session['respuestas_incorrectas'].append(request.POST)
            ctx['completo'] = True
    else:
        ctx['tipo'] = 'pregunta'
        for key in ['pregunta', 'respuesta_correcta', 'respuestas_incorrectas']:
            quitar_de_session(request, key)

    return render(request,template_name, ctx)

@login_required
@user_passes_test(es_admin, login_url = '/preguntas/', redirect_field_name = None)
def guardar(request):
    pregunta = extraer_data(request, 'pregunta')
    if pregunta is not None:
        texto_pregunta = pregunta.get('texto_pregunta')
        nivel = pregunta.get('nivel')
        p = Pregunta.objects.create(texto_pregunta = texto_pregunta, nivel = nivel)

        correcta = extraer_data(request, 'respuesta_correcta')
        if correcta is not None:
            crear_respuesta(p, correcta, True)

        incorrectas = extraer_data(request, 'respuestas_incorrectas')
        if incorrectas is not None:
            for incorrecta in incorrectas:
                crear_respuesta(p, incorrecta, False)

    return redirect('preguntas:listar')


def extraer_data(request, key):
    if key in request.session:
        data = request.session[key]
        del request.session[key]
        return data

def crear_respuesta(pregunta, respuesta, correcta):
    if respuesta is not None:
        texto_respuesta = respuesta.get('texto_respuesta')
        print(pregunta.respuesta_set.create(texto_respuesta = texto_respuesta, es_correcta = correcta))

def quitar_de_session(request, key):
    if key in request.session:
        del request.session[key]

def eliminar(request, pk):
    p = Pregunta.objects.get(id=pk)
    p.delete()
    return redirect("preguntas:listar")