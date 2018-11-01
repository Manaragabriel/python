from django import template

register= template.Library()



def trocar(value):
    return value.replace("-"," ")

register.filter("trocar",trocar)