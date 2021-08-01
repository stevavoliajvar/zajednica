# Generated by Django 2.2.7 on 2020-12-16 21:00

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_temp2_broj_stana'),
    ]

    operations = [
        migrations.AddField(
            model_name='temppapir',
            name='city',
            field=models.CharField(default='Belgrade', max_length=60),
        ),
        migrations.AddField(
            model_name='temppapir',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='44.79688084502436,20.477120876312256', max_length=63),
        ),
    ]