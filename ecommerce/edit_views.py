from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Endereco, User,Produto,Departamento
from .forms import Form_Departamento,Form_Endereco,Form_Produto,Form_User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/adm-login/')
def remove_dpt(request):
    if not request.user.is_staff:
        return redirect('/amd-login/')
    dpt= Departamento.objects.get(id=request.GET.get("id"))
    dpt.delete()
    return redirect('/departamentosadm/')

@login_required(login_url='/adm-login/')
def remove_produto(request):
    if not request.user.is_staff:
        return redirect('/amd-login/')
    prod= Produto.objects.get(id=request.GET.get("id"))
    prod.delete()
    return redirect('/produtosadm/')

@login_required(login_url='/adm-login/')
def edit_produto(request):
    if not request.user.is_staff:
        return redirect('/amd-login/')
    request.session["idp"]= request.GET.get("id")
    return render(request,'edit_produto.html',{"form": Form_Produto(instance=Produto.objects.get(id=request.GET.get("id")))})

@login_required()
def save_edit_prod(request):
    prod= Produto.objects.get(id=request.session["idp"])
    form= Form_Produto(request.POST,request.FILES, instance=prod)
    if form.is_valid() and request.user.is_staff:
        form.save()
        request.session["idp"]= None
        return redirect('/produtosadm/')
    else:
        return redirect('/error/')