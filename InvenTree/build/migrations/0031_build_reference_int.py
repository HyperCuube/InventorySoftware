# Generated by Django 3.2.5 on 2021-10-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0030_alter_build_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='reference_int',
            field=models.IntegerField(default=0),
        ),
    ]
