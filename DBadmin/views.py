from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Comuna

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
    #return HttpResponse(json.dumps(results), content_type="application/json")



#    return HttpResponse(element)
#    return render(request, '../templates/index.html')
