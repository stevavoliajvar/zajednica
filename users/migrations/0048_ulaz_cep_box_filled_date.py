# Generated by Django 2.2.7 on 2021-03-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_auto_20210310_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='ulaz',
            name='cep_box_filled_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
