# Generated by Django 2.2.7 on 2020-10-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201001_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='upravnik',
            name='firma',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
