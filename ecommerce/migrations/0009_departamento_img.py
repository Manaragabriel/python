# Generated by Django 2.1 on 2018-09-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_departamento_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='img',
            field=models.ImageField(default='padrao.png', upload_to=''),
        ),
    ]