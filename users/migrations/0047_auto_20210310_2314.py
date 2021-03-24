# Generated by Django 2.2.7 on 2021-03-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_auto_20210307_2315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grad',
            options={'verbose_name_plural': 'Gradovi'},
        ),
        migrations.AlterModelOptions(
            name='opština',
            options={'verbose_name_plural': 'Opštine'},
        ),
        migrations.AlterField(
            model_name='temp2',
            name='Grad',
            field=models.CharField(choices=[('Beograd', 'Beograd'), ('Novi Sad', 'Novi Sad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='temp2',
            name='Opština',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
