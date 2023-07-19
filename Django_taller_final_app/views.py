from django.shortcuts import render
from django.http import JsonResponse
from Django_taller_final_app.models import Participantes

# Create your views here.

def index(request):
    return render(request, 'index.html')


def guardar(request):
    emp = {
        'id':123,
        'nombre': 'Pedro',
        'email': 'pedro@gmail.com',
        'sueldo': 145555555
    }
    return JsonResponse(emp)

    # if request.method == 'POST':
    #     nombre = request.POST.get('nombre')
    #     apellido = request.POST.get('apellido')
    #     telefono = request.POST.get('telefono')
    #     fecha_inscripcion = request.POST.get('fecha_inscripcion')
    #     institucion = request.POST.get('institucion')
    #     hora_inscripcion = request.POST.get('hora_inscripcion')
    #     estado = request.POST.get('estado')
    #     observacion = request.POST.get('observacion')

    #     participante = Participantes(
    #         nombre=nombre,
    #         apellido=apellido,
    #         telefono=telefono,
    #         fecha_inscripcion=fecha_inscripcion,
    #         institucion=institucion,
    #         hora_inscripcion=hora_inscripcion,
    #         estado=estado,
    #         observacion=observacion
    #     )

    #     participante.save()
    #     return JsonResponse({'mensaje': 'Se guardo correctamente'})
    # else:
    #     return JsonResponse({'mensaje': 'No se guardo correctamente'})

def verPartipantes(request):
    participantes = Participantes.objects.all()
    data = { 'participantes': list(participantes.values()) }
    return JsonResponse(data)