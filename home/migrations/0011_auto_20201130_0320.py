# Generated by Django 2.2.7 on 2020-11-30 03:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20201130_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
