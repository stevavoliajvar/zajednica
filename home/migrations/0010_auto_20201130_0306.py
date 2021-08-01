# Generated by Django 2.2.7 on 2020-11-30 03:06

import ckeditor.fields
from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201124_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]