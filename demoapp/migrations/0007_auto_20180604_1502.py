# Generated by Django 2.0.6 on 2018-06-04 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_remove_assignments_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignments',
            old_name='title',
            new_name='heading',
        ),
    ]
