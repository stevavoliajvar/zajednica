# Generated by Django 2.2.7 on 2020-10-13 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20201013_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
