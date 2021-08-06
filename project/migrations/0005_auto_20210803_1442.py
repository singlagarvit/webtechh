# Generated by Django 3.2.5 on 2021-08-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_casestudy_alt_tag_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestudy',
            old_name='alt_tag_thumbnail',
            new_name='alt_tag_banner',
        ),
        migrations.RemoveField(
            model_name='casestudy',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='casestudy',
            name='banner',
            field=models.ImageField(null=True, upload_to='project/banners/'),
        ),
    ]