# Generated by Django 2.1 on 2018-10-23 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0023_pedido'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('is_staff', 'Is Staff')], 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
    ]
