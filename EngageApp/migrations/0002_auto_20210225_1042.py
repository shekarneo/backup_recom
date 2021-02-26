# Generated by Django 3.1.6 on 2021-02-25 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EngageApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpartners',
            name='dt_created_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='eventpartners',
            name='ft_amount_charged',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='eventpartners',
            name='last_modified_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='eventpartners',
            name='last_modified_empid',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='EventMediaPartner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vc_comapany_name', models.CharField(max_length=200)),
                ('vc_logo_link', models.CharField(max_length=400)),
                ('vc_status', models.CharField(max_length=200)),
                ('vc_priority', models.IntegerField()),
                ('vc_company_url', models.CharField(max_length=300)),
                ('vc_created_datetime', models.DateTimeField()),
                ('event', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EngageApp.eventdetails')),
            ],
        ),
    ]
