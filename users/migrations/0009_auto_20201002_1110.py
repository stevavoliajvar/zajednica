# Generated by Django 2.2.7 on 2020-10-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_is_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='radi_za',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vrsta_upravnika',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]