# Generated by Django 3.1.7 on 2021-03-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabapp', '0007_auto_20210318_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
