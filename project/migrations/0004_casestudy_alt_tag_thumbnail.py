# Generated by Django 3.2.5 on 2021-08-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_thumbnail_alt_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='alt_tag_thumbnail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]