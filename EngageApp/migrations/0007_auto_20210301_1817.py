# Generated by Django 3.1.6 on 2021-03-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EngageApp', '0006_auto_20210301_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getintouch',
            name='designation',
        ),
        migrations.AddField(
            model_name='getintouch',
            name='message',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='getintouch',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
