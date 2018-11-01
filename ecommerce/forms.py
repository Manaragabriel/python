from django import forms
from django.contrib.auth import get_user_model
from .models import Produto,Departamento,Endereco
User= get_user_model()


class Form_User(forms.ModelForm):
    password= forms.CharField(label='Senha',widget=forms.PasswordInput())
    password2= forms.CharField(label='Confirme a senha',widget=forms.PasswordInput())

    def clean_password2(self):
        password= self.cleaned_data.get("password")
        password2= self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Senhas diferentes")
        return password2

    def save(self,commit=True):
        user= super(Form_User,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    class Meta:
        model= User
        fields=["nome","email","tel","cpf"]

class Form_Departamento(forms.ModelForm):
    departamento= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    

    class Meta:
        model= Departamento
        fields=["departamento"]

class Form_Produto(forms.ModelForm):
    
    def clean_nome_produto(self):
        produto= self.clean_data.get("nome_produto")
        return produto.replace(" ","-")

    class Meta:
        model= Produto
        fields=["nome_produto","descricao","quantidade","preco","peso","dpt","altura","largura","marca","imagem","imagem2","imagem3","imagem4","imagem5","imagem6"]
        widgets={
            "nome_produto": forms.TextInput(attrs={"class":"form-control"}),
            "descricao": forms.Textarea(attrs={"class":"form-control"}),
            "quantidade": forms.NumberInput(attrs={"class":"form-control"}),
            "preco": forms.NumberInput(attrs={"class":"form-control"}),
            "peso": forms.NumberInput(attrs={"class":"form-control"}),
            "altura": forms.NumberInput(attrs={"class":"form-control"}),
            "largura": forms.NumberInput(attrs={"class":"form-control"}),
            "marca": forms.TextInput(attrs={"class":"form-control"}),
           
         
        }


        
class Form_Endereco(forms.ModelForm):

    class Meta:
        model= Endereco
        #fields= ["cep","rua","numero","bairro","cidade","estado","cliente"]
        exclude=["cliente"]
        widgets={
            "cep": forms.NumberInput(attrs={"class":"form-control"}),
            "rua": forms.TextInput(attrs={"class":"form-control"}),
            "numero": forms.NumberInput(attrs={"class":"form-control"}),
            "referencia": forms.TextInput(attrs={"class":"form-control"}),
            "bairro": forms.TextInput(attrs={"class":"form-control"}),
            "cidade": forms.TextInput(attrs={"class":"form-control"}),
            "estado": forms.TextInput(attrs={"class":"form-control"}),
           # "cliente": forms.HiddenInput(attrs={"value":"{{request.user.id}}"})
        }
    