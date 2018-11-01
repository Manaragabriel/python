from django.contrib import admin
from .models import Produto, User,Departamento

admin.site.register(Produto)
admin.site.register(Departamento)
admin.site.register(User)
# Register your models here.
