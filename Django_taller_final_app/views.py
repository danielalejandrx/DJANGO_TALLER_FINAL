from django.shortcuts import render
from django.http import JsonResponse
from Django_taller_final_app.models import Participantes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import ParticipanteSerial
from rest_framework.decorators import api_view

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



#CLASS BASED VIEW

class ParticipanteList(APIView):
    def get(self, request):
        participante=Participantes.objects.all()
        serial = ParticipanteSerial(participante, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = ParticipanteSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipanteDetalle(APIView):
    def get_object(self, pk):
        try:
            return Participantes.objects.get(pk=pk)
        except Participantes.DoesNotExist:
            return Http404

    def get(self, request, pk):
        partipante = self.get_object(pk)
        serial = ParticipanteSerial(partipante)
        return Response(serial.data)

    def put(self, request, pk):
        participante = self.get_object(pk)
        serial = ParticipanteSerial(participante, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk):
        participante = self.get_object(pk)
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    #FUNCTION BASED VIEW
@api_view(['GET', 'POST'])
def participante_list(request):
    if request.method == 'GET':
        participante = Participantes.objects.all()
        serial = ParticipanteSerial(participante, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = ParticipanteSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def participante_detalle(request, id):
    try:
        participante = Participantes.objects.get(pk=id)
    except participante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = ParticipanteSerial(participante)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = ParticipanteSerial(participante, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)