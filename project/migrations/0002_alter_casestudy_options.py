# Generated by Django 3.2.5 on 2021-07-30 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casestudy',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Case studies'},
        ),
    ]
