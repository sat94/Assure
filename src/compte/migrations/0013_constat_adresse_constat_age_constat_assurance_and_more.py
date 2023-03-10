# Generated by Django 4.1.5 on 2023-03-09 14:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0012_remove_constat_adresse_remove_constat_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='constat',
            name='adresse',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='assurance',
            field=models.CharField(blank=True, choices=[('1', 'Assureplus'), ('2', 'Direct Assurance'), ('3', 'Eurofils'), ('4', 'MMA'), ('5', 'Active Assurance'), ('6', 'Acomme Assurance'), ('7', 'MAAF'), ('8', 'Allianz'), ('9', "L'olivier Assurance"), ('10', 'Leocare'), ('11', 'SOS Malus'), ('12', 'Lablette'), ('13', 'AXA'), ('15', 'Matmut'), ('16', 'Cardif'), ('17', 'SwissLife'), ('18', 'MAIF'), ('19', 'AMF'), ('20', 'LCL Assurance'), ('21', 'GROUPAMA'), ('22', 'April'), ('23', 'GENERAL ASSURANCE'), ('24', 'AVIVA'), ('25', 'Banque Postale'), ('26', 'Carrefour ASSURANCE'), ('27', 'AGPM')], max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='circonstance',
            field=models.ManyToManyField(max_length=20, to='compte.accident'),
        ),
        migrations.AddField(
            model_name='constat',
            name='code_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='commentaireA',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='commentaireB',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='couleur',
            field=models.CharField(blank=True, choices=[('Rouge', 'Rouge'), ('Gris', 'Gris'), ('Blanche', 'Blanche'), ('Bleu', 'Bleu'), ('Noire', 'Noire'), ('Jaune', 'Jaune'), ('Verte', 'Verte'), ('Maron', 'Maron'), ('Violette', 'Violette'), ('Rose', 'Rose'), ('Beige', 'Beige'), ('Silver', 'Silver')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degat_vehicule_a',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degat_vehicule_b',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degatautre',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degatouA',
            field=models.CharField(blank=True, choices=[('devant', 'devant'), ('arriere', 'arriere'), ('coter droit', 'coter droit'), ('coter gauche', 'coter gauche')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degatouB',
            field=models.CharField(blank=True, choices=[('devant', 'devant'), ('arriere', 'arriere'), ('coter droit', 'coter droit'), ('coter gauche', 'coter gauche')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degatsA',
            field=models.CharField(blank=True, choices=[('1', 'dégat sur mon véhicule'), ('2', "dégat sur l'autre véhicule"), ('3', 'dégat sur véhicule autre que A et B'), ('4', 'dégat sur objet autre que A et B')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='degatsB',
            field=models.CharField(blank=True, choices=[('1', 'dégat sur mon véhicule'), ('2', "dégat sur l'autre véhicule"), ('3', 'dégat sur véhicule autre que A et B'), ('4', 'dégat sur objet autre que A et B')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='lieu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.ville'),
        ),
        migrations.AddField(
            model_name='constat',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='modeles',
            field=models.ForeignKey(blank=True, max_length=20, null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.modele'),
        ),
        migrations.AddField(
            model_name='constat',
            name='nbCirconstance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='nbcontrat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='nbpermis',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='personne',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='constat',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[250, 350], upload_to='photo'),
        ),
        migrations.AddField(
            model_name='constat',
            name='plaque',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='prenom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='signature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constat',
            name='tel',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AddField(
            model_name='constat',
            name='temoin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='typee',
            field=models.CharField(blank=True, choices=[('Berline', 'berline'), ('Coupée', 'Coupée'), ('Hayon', 'Hayon'), ('Pick-up', 'Pick-up'), ('Crossover', 'Crossover'), ('SUV', 'SUV'), ('Fourgonettes', 'Fourgonettes'), ('Cabriolets', 'Cabriolets'), ('Roadsters', 'Roadsters'), ('Targa', 'Targa')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constat',
            name='voiture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.marque'),
        ),
    ]
