# Generated by Django 2.0.6 on 2018-06-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='submission',
            name='description',
            field=models.TextField(),
        ),
    ]
