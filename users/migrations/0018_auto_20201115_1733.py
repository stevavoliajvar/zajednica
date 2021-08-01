# Generated by Django 2.2.7 on 2020-11-15 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20201115_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Ulica_i_broj',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='radi_za',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CustomUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vrsta_upravnika',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ulaz',
            name='Grad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ulaz',
            name='Opština',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ulaz',
            name='Ulica_i_broj',
            field=models.CharField(max_length=100),
        ),
    ]