# Generated by Django 2.2.7 on 2020-10-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201001_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prosecna_ocena',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
