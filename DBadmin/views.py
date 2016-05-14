from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Comuna, Hospital, Paciente
from django.core import serializers
import json

# Create your views here.

@login_required
def userdata(request):
    to_json = {
        "email": request.user.email,
        "username": request.user.username,
        "firstname": request.user.first_name,
        "lastname": request.user.last_name
    }
    return JsonResponse(to_json)

@login_required
def comunas(request):
    resultset = Comuna.objects.all()
    results = [ob.as_json() for ob in resultset]
    return JsonResponse(results, safe=False)

@login_required
def hospitales(request):
    resultset = Hospital.objects.all()
    results = [ob.as_json() for ob in resultset]
    return JsonResponse(results, safe=False)

@login_required
def gruposSanguineos(request):
    data = [{'id': sang[0], 'grupo': sang[1]} for sang in Paciente.op_grupo_sang]
    return JsonResponse(data, safe=False)


#    return HttpResponse(element)
#    return render(request, '../templates/index.html')
