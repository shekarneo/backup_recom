# Generated by Django 3.1.6 on 2021-02-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EngageApp', '0003_coupens'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventconference_1',
            name='coupen',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='virtualregister',
            name='coupen',
            field=models.CharField(default='', max_length=200),
        ),
    ]
