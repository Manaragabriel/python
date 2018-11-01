from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser,PermissionsMixin):
    username= models.CharField(max_length=100)
    email= models.EmailField("Seu email",max_length=100,unique=True)
    tel= models.IntegerField("Telefone",default=0)
    nome= models.CharField(max_length=100)
    is_staff= models.BooleanField(default=False,blank=True)
    is_active= models.BooleanField(default=True,blank=True)
    data_joined= models.DateTimeField(auto_now_add= True)
    cpf= models.IntegerField()

    objects= UserManager()
    USERNAME_FIELD= 'email'
    #REQUIRED_FIELDS=['email']

    def get_full_name(self):
        return str(self)

    def __str__(self):
        return self.nome or self.username

    def get_short_name(self):
        return self.nome

    class Meta:
        verbose_name= "Usuário"
        verbose_name_plural= "Usuários"
        permissions=[
            ('is_staff',"Is Staff")
        ]

class Endereco(models.Model):
    cep= models.IntegerField()
    rua= models.CharField(max_length=50)
    numero= models.IntegerField()
    referencia= models.CharField(max_length=50)
    bairro= models.CharField(max_length=50)
    cidade= models.CharField(max_length=50)
    estado= models.CharField(max_length=2)
    cliente= models.ForeignKey(User,on_delete=models.CASCADE)

class Departamento(models.Model):
    departamento= models.CharField(max_length=100)
    img= models.ImageField()

    def __str__(self):
        return self.departamento

class Produto(models.Model):
    nome_produto= models.CharField(max_length=100)
    preco= models.DecimalField(decimal_places=2,max_digits=10)
    quantidade= models.IntegerField()
    descricao= models.TextField()
    peso= models.DecimalField(decimal_places=2,max_digits=10)
    imagem= models.ImageField()
    imagem2= models.ImageField(default="padrao.png")
    imagem3= models.ImageField(default="padrao.png")
    imagem4= models.ImageField(default="padrao.png")
    imagem5= models.ImageField(default="padrao.png")
    imagem6= models.ImageField(default="padrao.png")
    dpt= models.ForeignKey(Departamento,on_delete= models.CASCADE)
    largura= models.IntegerField()
    altura= models.IntegerField()
    marca= models.CharField(max_length=50)
    qtdvendas= models.IntegerField(default=0)

    class Meta:
        indexes=[
            models.Index(fields=['nome_produto'])
        ]

    
class Pedido(models.Model):
    produto= models.ForeignKey(Produto,on_delete= models.CASCADE)
    cliente= models.ForeignKey(User,on_delete=models.CASCADE)
    qtd= models.IntegerField(default=1)