# Generated by Django 2.2.7 on 2021-10-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageNotificationsBucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty', models.BooleanField(default=True)),
            ],
        ),
    ]
