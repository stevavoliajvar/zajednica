# Generated by Django 2.2.7 on 2021-03-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_auto_20210307_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='ulaz',
            name='Grad',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ulaz',
            name='Opština',
            field=models.CharField(max_length=50, null=True),
        ),
    ]