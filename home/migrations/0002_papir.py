# Generated by Django 2.2.7 on 2020-10-03 15:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profile_o_sebi'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolicina', models.IntegerField(blank=True, null=True)),
                ('datum', models.DateTimeField(default=django.utils.timezone.now)),
                ('ulaz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Ulaz')),
            ],
        ),
    ]
