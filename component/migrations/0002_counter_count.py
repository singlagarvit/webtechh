# Generated by Django 3.2.5 on 2021-08-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
