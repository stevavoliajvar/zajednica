# Generated by Django 2.2.7 on 2020-12-23 08:57

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_auto_20201222_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ulaz',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]