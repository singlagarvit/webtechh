# Generated by Django 3.2.5 on 2021-07-29 21:10

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('banner', models.ImageField(upload_to='pages/static/banners/')),
                ('tagline', models.CharField(blank=True, max_length=80, null=True)),
                ('button', models.CharField(blank=True, max_length=20, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('seo_tag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.seotag')),
            ],
        ),
        migrations.CreateModel(
            name='PageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pages/static/images/')),
                ('content', ckeditor.fields.RichTextField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.staticpage')),
            ],
        ),
        migrations.CreateModel(
            name='FooterPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=100, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('seo_tag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.seotag')),
            ],
        ),
    ]
