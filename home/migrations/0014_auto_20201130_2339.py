# Generated by Django 2.2.7 on 2020-11-30 23:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20201130_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='Sadržaj',
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True,
                null=True
            ),
        ),
    ]
