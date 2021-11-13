# Generated by Django 2.2.7 on 2020-10-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_papir_cena'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tip',
            field=models.CharField(
                choices=[
                    ('Warning', 'Warning'),
                    ('Info', 'Info')
                ],
                default='Info',
                max_length=50
            ),
        ),
    ]
