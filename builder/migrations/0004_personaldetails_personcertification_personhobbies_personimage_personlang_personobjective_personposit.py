# Generated by Django 3.2.3 on 2021-06-03 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20210602_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Position Name')),
                ('duration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Working Period')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('skill', models.CharField(max_length=255, verbose_name='Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=100, verbose_name='CheckID')),
                ('qualification', models.CharField(blank=True, max_length=255, null=True, verbose_name='Qualification')),
                ('institution', models.CharField(blank=True, max_length=100, null=True, verbose_name='College/School')),
                ('passed', models.IntegerField(verbose_name='Passing Year')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Project Name')),
                ('details', models.TextField(verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Place')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('details', models.TextField(verbose_name='Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('aim', models.TextField(blank=True, null=True, verbose_name='Objective')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(blank=True, max_length=255, null=True, verbose_name='Known Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonHobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('hobby', models.CharField(blank=True, max_length=255, null=True, verbose_name='Hobby')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=100, verbose_name='CheckID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Certificates Name')),
                ('institution', models.CharField(blank=True, max_length=100, null=True, verbose_name='Institution Name')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('details', models.TextField(verbose_name='Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Person Name')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact', models.PositiveIntegerField(verbose_name='Contact')),
                ('profile', models.URLField(blank=True, null=True, verbose_name='Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
