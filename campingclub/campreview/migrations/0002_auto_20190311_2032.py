# Generated by Django 2.1.4 on 2019-03-11 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campreview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campsitefeatures',
            old_name='view',
            new_name='viewtype',
        ),
    ]
