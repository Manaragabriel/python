from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .forms import Form_User,Form_Produto, Form_Departamento, Form_Endereco
from .models import User,Produto,Departamento,Endereco,Pedido
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.core.mail import send_mail
from django import template
# Create your views here.




def teste(request):
    produto= Produto.objects.get(id=10)
    return HttpResponse()

def index(request):
    produtos= Produto.objects.all().order_by('id').reverse()[:8]
    return render(request,"index.html",{"produtos": produtos,"menu_dpt": Departamento.objects.all()})


@login_required(login_url='/adm-login/')
def paineladm(request):
    
    if not request.user.is_staff:
        return redirect('/adm-login/')
    
    return render(request,'paineladm.html')

@login_required(login_url='/adm-login/')
def departamentosadm(request):
    if not request.user.is_staff:
        return redirect('/adm-login/')
    return render(request,"departamentosadm.html",{"form": Form_Departamento(),"dpts": Departamento.objects.all()})

@login_required(login_url='/adm-login/')
def produtosadm(request):
    if not request.user.is_staff:
        return redirect('/adm-login/')
    return render(request,"produtosadm.html",{"form":Form_Produto(),"dpts":Departamento.objects.all(),"prod":Produto.objects.all()})


    
def adm_login(request):
  
    return render(request,'adm-login.html')

def cadastro(request):
    return render(request,"cadastro.html",{"form": Form_User(),"menu_dpt": Departamento.objects.all()})


def cliente_login(request):
    return render(request,'cliente_login.html',{"menu_dpt": Departamento.objects.all()})

@login_required(login_url='/cliente_login/')
def paineluser(request):
  
    return render(request,'paineluser.html',{"menu_dpt": Departamento.objects.all()})

@login_required(login_url='/cliente_login/')
def cliente_info(request):
    endereco= Endereco.objects.filter(cliente= request.user)
    return render(request,"cliente_info.html",{"form":Form_User(instance= request.user),"form_end":Form_Endereco(),"enderecos":endereco})

def buscar(request,pesquisa):

    return render(request,'pesquisar.html',{"data":Produto.objects.filter(nome_produto__icontains=pesquisa.replace("-"," ")),"menu_dpt": Departamento.objects.all()})

def produto(request,produto):
    return render(request,'produto.html',{"data": Produto.objects.get(nome_produto=produto),"menu_dpt": Departamento.objects.all()})

def carrinho(request):
    pedido= Pedido.objects.filter(cliente=request.user)
    total = int()
    for p in pedido:
        total += p.produto.preco*p.qtd
    return render(request,'carrinho.html',{"dados": pedido,"menu_dpt": Departamento.objects.all(),"total":total})


@login_required(login_url='/cliente_login/')
def addcarrinho(request,id):
    pedido= Pedido()
    produto= Produto.objects.get(id=id)
    pedido.produto= produto
    pedido.cliente= request.user
    pedido.qtd= 1
    pedido.save()
    return redirect('/carrinho/')

@login_required(login_url='/cliente_login/')
def remove_carrinho(request,id):
   
    pedido= Pedido.objects.get(id=id,cliente=request.user)
    pedido.delete()
    return redirect('/carrinho/')

def sair(request):
    logout(request)
    return redirect('/cliente_login/')



@login_required()
def cadproduto(request):
    
    form= Form_Produto(request.POST,request.FILES)
    if form.is_valid() and request.user.is_staff:
        form.save()
        return redirect('/produtosadm/')
    else:
        return redirect('/error/')




def departamento(request,departamento):
    
    return render(request,"departamento.html",{"menu_dpt": Departamento.objects.all(),"data": Produto.objects.filter(dpt__departamento=departamento)})