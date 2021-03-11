# Generated by Django 3.1.6 on 2021-03-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EngageApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupons',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventassociation',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventconference_1',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventdates',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventdelegates',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventexhibitor',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventexhibitor_1',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventmediapartner',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventpartners',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventpartnerships',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventsalespersons',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventspeakers',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventsupportedby',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventtestimonials',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventvisitor_1',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventvisitors',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='gallary',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='virtualregister',
            old_name='event',
            new_name='event_id',
        ),
        migrations.AddField(
            model_name='masterevent',
            name='news',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='masterevent',
            name='presentation',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
