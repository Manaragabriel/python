function cadproduto(){
   
    $.ajax({
        type: "POST",
        url: "/cadproduto/",
        data: $("#formprod").serializeArray(),
        cache: false,
      
        
    }).done(function(resp){
        if(!resp.confirmacao){
            alert("erro ao cadastrar");
        }else{
            location.href="http://localhost:8000/etapa2/"+resp.confirmacao;
        }
    });
}
function caddepartamento(){
    $.ajax({
        type: "POST",
        url: '/caddpt/',
        data: $('#formdpt').serializeArray(),
        cache: false,
    }).done(function(resp){
        if (!resp.confirmacao){
            alert("Erro");
        }else{
            location.href='/departamentosadm/';
        }
    });
}

function caduser(url,form,redirect){
    $.ajax({
        url: url,
        type: "POST",
        data: $(form).serializeArray(),
        cache: false,
    }).done(function(resp){
        if(!resp.confirmacao){
            alert("Houve um erro"+resp.e);
        }else{
            location.href=redirect;
            
        }
    });
}
function login(url,form,redirect){
    $.ajax({
        url: url,
        type: 'POST',
        data: $(form).serializeArray(),
        cache: false,
    }).done(function(resp){
        if(!resp.confirmacao){
            alert(resp.retorno);
        }else{
            location.href= redirect;
        }
    });

}
function cadastros(url,form,redirect){
    $.ajax({
        url: url,
        type: 'POST',
        data: $(form).serializeArray(),
        cache: false,
    }).done(function(resp){
        if(!resp.confirmacao){
            alert(resp.retorno);
        }else{
            location.href= redirect;
        }
    });
}

function pesquisar(){
    var search= document.getElementById("name").value;

    window.location.href= "http://localhost:8000/buscar/"+search.replace(" ","-");
}

function addcarrinho(id){
    location.href= "/addcarrinho/"+id;

}
function recuperar(){
    $.ajax({
        url: '/recuperar-senha/',
        type: 'POST',
        data: $('#recupera').serializeArray(),
        cache: false,
    }).done(function(resp){
        alert("Nova senha enviada ao seu e-mail");
    });
}