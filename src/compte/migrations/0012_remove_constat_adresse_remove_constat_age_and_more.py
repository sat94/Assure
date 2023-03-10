# Generated by Django 4.1.5 on 2023-03-09 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0011_remove_constat_personne'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constat',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='age',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='assurance',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='circonstance',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='code_postal',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='commentaireA',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='commentaireB',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='couleur',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='date',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degat_vehicule_a',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degat_vehicule_b',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degatautre',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degatouA',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degatouB',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degatsA',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='degatsB',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='lieu',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='modeles',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='nbCirconstance',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='nbcontrat',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='nbpermis',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='plaque',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='temoin',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='typee',
        ),
        migrations.RemoveField(
            model_name='constat',
            name='voiture',
        ),
    ]