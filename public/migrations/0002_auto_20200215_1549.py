# Generated by Django 2.2.6 on 2020-02-15 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicdata',
            old_name='area',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='publicdata',
            old_name='fname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='publicdata',
            old_name='lname',
            new_name='state',
        ),
    ]