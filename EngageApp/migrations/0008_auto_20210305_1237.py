# Generated by Django 3.1.6 on 2021-03-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EngageApp', '0007_auto_20210301_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventspeakers',
            name='presentation',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='eventspeakers',
            name='vidio_url',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
