from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, '../templates/index.html', {'user': request.user})

# Create your views here.
