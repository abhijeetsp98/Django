# Generated by Django 2.1.7 on 2020-03-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20200215_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicdata',
            name='ready',
            field=models.BooleanField(default=False),
        ),
    ]
