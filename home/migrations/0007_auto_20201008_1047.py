# Generated by Django 2.2.7 on 2020-10-08 10:47

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('home', '0006_auto_20201006_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags'
            ),
        ),
    ]
