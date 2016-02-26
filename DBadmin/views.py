from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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


#    return HttpResponse(element)
#    return render(request, '../templates/index.html')
