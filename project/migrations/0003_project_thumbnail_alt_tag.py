# Generated by Django 3.2.5 on 2021-08-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_casestudy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail_alt_tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]