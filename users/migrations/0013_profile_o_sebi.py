# Generated by Django 2.2.7 on 2020-10-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201002_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='o_sebi',
            field=models.TextField(blank=True, null=True),
        ),
    ]