# Generated by Django 3.2.3 on 2021-06-02 11:50

import builder.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_name', models.CharField(max_length=255, unique=True, verbose_name='Template Name')),
                ('resume_image', models.ImageField(upload_to='', verbose_name='Resume Image')),
                ('resume_uid', models.CharField(default=builder.models.ruid, editable=False, max_length=8, unique=True, verbose_name='UID')),
                ('resume_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.type')),
            ],
        ),
    ]
