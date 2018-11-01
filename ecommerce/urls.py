from django.urls import path,re_path
from . import views
from . import ajax
from . import edit_views


urlpatterns = [
    path('',views.index),
    path('paineladm/',views.paineladm),
    path('departamentosadm/',views.departamentosadm),
    path('teste/',views.teste),
    path('produtosadm/',views.produtosadm),
    path('caddpt/',ajax.caddpt),
    path('cadproduto/',views.cadproduto),
    path('cadastro/',views.cadastro),
    path('caduser/',ajax.caduser),
    path('paineluser/',views.paineluser),
    path('cliente_login/',views.cliente_login),
    path('login_user/',ajax.login_user),
    path('cad_endereco/',ajax.cad_endereco),
    re_path(r'^buscar/(?P<pesquisa>[\w-]+)/',views.buscar),
    #path('produto/<slug:produto>/',views.produto),
    re_path(r'^produto/(?P<produto>[\w|\W]+)/', views.produto),
    path('carrinho/',views.carrinho),
    re_path(r'^addcarrinho/(?P<id>[\w|\W]+)/',views.addcarrinho),
    path('remove-carrinho/<slug:id>',views.remove_carrinho),
    path('sair/',views.sair),
    path('recuperar-senha/',ajax.recuperar_senha),
    path('adm-login/',views.adm_login),
    path('remove_dpt/',edit_views.remove_dpt),
    path('remove_produto/',edit_views.remove_produto),
    path('edit_produto/',edit_views.edit_produto),
    path('save_edit_prod/',edit_views.save_edit_prod),
    re_path(r'^departamento/(?P<departamento>[\w-]+)/',views.departamento),
    path('cliente_info/',views.cliente_info),
    
        
]