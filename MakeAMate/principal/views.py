from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

def login_view(request):
    template='loggeos/login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
    else:
        form = AuthenticationForm()
    return render(request,template,{'form':form})
   
def notification_view(request):
    template='notificacion.html'