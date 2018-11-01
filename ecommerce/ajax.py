from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Produto,Departamento,Endereco,User
from .forms import Form_Produto, Form_Departamento,Form_User,Form_Endereco
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random, string

@login_required()
def caddpt(request):
    form= Form_Departamento(request.POST)
    if form.is_valid() and request.user.is_staff:
        form.save()
        return JsonResponse({"confirmacao": True})
    else:
        return JsonResponse({"confirmacao":False})


def caduser(request):
    form= Form_User(request.POST)
    if form.is_valid():
        form.save()
        user=authenticate(username=request.POST.get("email"),password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            return JsonResponse({"confirmacao": True})
        else:
            return JsonResponse({"confirmacao": False}) 
            
    else:
        return JsonResponse({"confirmacao": False})
    

def login_user(request):
    user= authenticate(username=request.POST.get("email"),password=request.POST.get("password"))
    if user is not None:
        login(request,user)
        return JsonResponse({"confirmacao": True})
    else:
        return JsonResponse({"confirmacao":False,"retorno":"Email ou senha inválidos"})

@login_required()
def cad_endereco(request):
  
    form= Form_Endereco(request.POST)
    if form.is_valid() and request.user.id is not None:
        end=form.save(commit=False)
        end.cliente=request.user
        end.save()
        return JsonResponse({"confirmacao":True})
    else:
        return JsonResponse({"confirmacao":False,"retorno":"Não foi possivel cadastrar endereço"})

def recuperar_senha(request):
    user= User.objects.get(email=request.POST.get("email"))
    if user is not None:
        newpass=str()
        for n in range(0,random.randint(6,10)):
            newpass += random.choice(string.ascii_letters)
        user.set_password(newpass)
        user.save()
        send_mail("Lembrete de senha","Sua nova senha é:"+newpass,"Loja Virtual",[request.POST.get("email")],fail_silently=False)
        return JsonResponse({"confirmacao":True})
    else:
        return JsonResponse({"confirmacao":False,"ret":"Digite um email cadastrado"})