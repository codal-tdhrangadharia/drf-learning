# Generated by Django 2.0.6 on 2018-06-04 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_auto_20180604_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='demoapp.assignments'),
            preserve_default=False,
        ),
    ]
