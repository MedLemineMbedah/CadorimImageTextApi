# Generated by Django 4.0.3 on 2022-03-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadorimrest', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='nationalite',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tpe_de_cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='Nom',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='NumeroDocument',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='Path',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='Pays',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='Rue',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='Sex',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='Ville',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='codePostale',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='dateEmission',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='dateValidie',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='date_naiss',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='lieu_de_nai',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='typeDocument',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='NNI',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Prenom',
            field=models.CharField(default='0000000', max_length=100),
        ),
    ]
