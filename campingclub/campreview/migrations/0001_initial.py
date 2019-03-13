# Generated by Django 2.1.4 on 2019-03-11 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'Campground',
            },
        ),
        migrations.CreateModel(
            name='Campsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loop', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'Campsite',
            },
        ),
        migrations.CreateModel(
            name='CampsiteFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.CharField(max_length=100)),
                ('trees', models.CharField(max_length=100)),
                ('partysize', models.IntegerField()),
                ('privacy', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'CampsiteFeatures',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featurename', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Features',
            },
        ),
        migrations.AddField(
            model_name='campsite',
            name='campsitefeatures',
            field=models.ManyToManyField(to='campreview.CampsiteFeatures'),
        ),
        migrations.AddField(
            model_name='campsite',
            name='siteID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='campreview.Campground'),
        ),
        migrations.AddField(
            model_name='campground',
            name='features',
            field=models.ManyToManyField(to='campreview.Features'),
        ),
    ]