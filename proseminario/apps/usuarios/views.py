from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb

# Create your views here.
def pagina_principal(request):
	
	return render_to_response("blog/principal.html",RequestContext(request))
def registro_usuario(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("/blog/")
	form=UserCreationForm()
	return render_to_response("usuario/registro.html",{"form":form},RequestContext(request))
	