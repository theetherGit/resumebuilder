# Generated by Django 3.2.3 on 2021-06-06 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0007_auto_20210606_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAcademicQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=255, verbose_name='Qualification')),
                ('institution', models.CharField(max_length=100, verbose_name='College/School')),
                ('passed', models.IntegerField(verbose_name='Passing Year')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonCareerObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aim', models.TextField(verbose_name='Objective')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonCertificationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Certificates Name')),
                ('institution', models.CharField(max_length=100, verbose_name='Institution Name')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('details', models.TextField(verbose_name='Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Person Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact', models.BigIntegerField(verbose_name='Contact')),
                ('profile', models.URLField(verbose_name='Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonHobbie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=255, verbose_name='Hobby')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonKnownLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=255, verbose_name='Known Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('details', models.TextField(verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255, verbose_name='Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonWorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('position', models.CharField(max_length=100, verbose_name='Position Name')),
                ('duration', models.CharField(max_length=100, verbose_name='Working Period')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('details', models.TextField(verbose_name='Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='personcertification',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personhobbies',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personimage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personlanguage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personobjective',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personprojects',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personqualification',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personskills',
            name='user',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personposition',
            name='user_cid',
        ),
        migrations.AlterField(
            model_name='personposition',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='personposition',
            name='place',
            field=models.CharField(max_length=100, verbose_name='Place'),
        ),
        migrations.DeleteModel(
            name='PersonalDetail',
        ),
        migrations.DeleteModel(
            name='PersonCertification',
        ),
        migrations.DeleteModel(
            name='PersonHobbies',
        ),
        migrations.DeleteModel(
            name='PersonImage',
        ),
        migrations.DeleteModel(
            name='PersonLanguage',
        ),
        migrations.DeleteModel(
            name='PersonObjective',
        ),
        migrations.DeleteModel(
            name='PersonProjects',
        ),
        migrations.DeleteModel(
            name='PersonQualification',
        ),
        migrations.DeleteModel(
            name='PersonSkills',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]