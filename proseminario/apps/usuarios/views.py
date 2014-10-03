from django.shortcuts import render,render_to_response
from django.template import RequestContext
import datetime

from .models import *

# Create your views here.
def pagina_principal(request):
	
	return render_to_response("blog/principal.html",RequestContext(request))
def registro_usuario(request):
	
	return render_to_response("usuario/registro.html",RequestContext(request))