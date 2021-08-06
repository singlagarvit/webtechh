# Generated by Django 3.2.5 on 2021-08-02 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
        ('component', '0004_whychooseussection'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tagline', models.CharField(blank=True, max_length=120, null=True)),
                ('background', models.ImageField(upload_to='component/case-studies/background/')),
                ('seo_tag', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.seotag')),
                ('site', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.site')),
            ],
            options={
                'verbose_name_plural': 'Case studies',
            },
        ),
    ]
