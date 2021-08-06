# Generated by Django 3.2.5 on 2021-08-02 10:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('component', '0003_alter_counter_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseUsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField()),
                ('site', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.site')),
            ],
        ),
    ]
