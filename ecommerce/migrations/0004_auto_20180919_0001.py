# Generated by Django 2.1 on 2018-09-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20180918_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.IntegerField(default=0, verbose_name='Telefone'),
        ),
    ]