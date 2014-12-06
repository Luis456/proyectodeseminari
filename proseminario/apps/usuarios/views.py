from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime

from .models import *
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.sessions.backends.db import SessionStore
import pdb
from .forms import *

# Create your views here.
def pagina_principal(request):
	
	return render_to_response("blog/principal.html",RequestContext(request))
def registro_usuario(request):
	menu=permisos(request)
	if request.method=="POST":
		form=fusuario(request.POST)
		if(form.is_valid()):
			usuario_nuevo=request.POST['username']
			form.save()
			usuario=User.objects.get(username=usuario_nuevo)
			perfil=Perfil.objects.create(user=usuario)
			#usuario.email=request.POST['email']
			#usuario.save

			return HttpResponseRedirect("/blog/")
	form=fusuario()
	return render_to_response("usuario/registro.html",{"menu":menu,"form":form},RequestContext(request))
def login_usuario(request):
	menu=permisos(request)
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/blog/active/")
			else:
				request.session['cont']=request.session['cont']+1
				aux=request.session['cont']
				estado=True
				mensaje="Error en los datos "+str(aux)
				if aux>3:
					formulario2=fcapcha()
					datos={'form':form,'formulario2':formulario2,'estado':estado,'mensaje':mensaje}
				else:
					datos={'form':form,'estado':estado,'mensaje':mensaje}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
	else:
		request.session['cont']=0
		form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"menu":menu,"form":form},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/blog/")
def perfil(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		usuario=request.user
		u=User.objects.get(username=usuario)
		try:
			perfil=Perfil.objects.get(user=u)
			request.session["name"]=u.username
		except Perfil.DoesNotExist:
			perfil=Perfil.objects.create(user=usuario)
			request.session["name"]=u.username
		if request.method=="POST":
			u=User.objects.get(username=usuario)
			perfil=Perfil.objects.get(user=u)

			formulario=fperfil(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return render_to_response("usuario/perfil.html",{"menu":menu,"nombre":request.session["name"]},RequestContext(request))
		else:
			formulario=fperfil()
		return render_to_response("usuario/perfil.html",{"menu":menu,"nombre":request.session["name"],"formulario":formulario},RequestContext(request))
	else:
		return HttpResponseRedirect("/blog/error/")
def active_los(request):
	
	return render_to_response("usuario/active.html",RequestContext(request))

def editar_perfil(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		u=request.user
		usuario=User.objects.get(username=u)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=="POST":
			formulario=fperfil_modificar(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/blog/active/")
		else:
			formulario=fperfil_modificar(instance=perfil)
			return render_to_response("usuario/modificarperfil.html",{"menu":menu,"formulario":formulario},RequestContext(request))
	else:
		return HttpResponseRedirect("/blog/")


def error_vista(request):
	
	return render_to_response("usuario/error.html",RequestContext(request))
def permisos(request):
	listadepermisos=[]
	
	listadepermisos.append({"url":"/blog/chat/","label":"Chat"})
	
	return listadepermisos	
def chat(request):
	idsession=request.session["idkey"]
	return HttpResponseRedirect("http://localhost:3000/django/"+idsession)