# Generated by Django 5.0.3 on 2024-03-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ref_codes',
            field=models.ManyToManyField(default=[], to='users.refcode'),
        ),
    ]
