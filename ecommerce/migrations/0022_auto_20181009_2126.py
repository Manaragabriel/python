# Generated by Django 2.1 on 2018-10-10 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_produto_qtdvendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]