# Generated by Django 2.2.7 on 2020-11-30 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_ulaz_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ulaz',
            name='website',
            field=models.URLField(default='https://www.b92.net/'),
        ),
    ]
