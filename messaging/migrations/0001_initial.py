# Generated by Django 2.2.7 on 2022-01-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageForUpravnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(null=True)),
                ('seen', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MessageNotificationsBucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty', models.BooleanField(default=True)),
            ],
        ),
    ]
