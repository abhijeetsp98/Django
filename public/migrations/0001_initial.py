# Generated by Django 2.2.6 on 2020-02-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('voted', models.BooleanField(default=False)),
                ('pic', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
