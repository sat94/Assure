# Generated by Django 4.1.5 on 2023-03-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_rename_commentaire_constat_commentairea_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='constat',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]