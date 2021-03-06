# Generated by Django 3.2.3 on 2021-06-06 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_alter_personaldetails_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cid', models.CharField(max_length=10, verbose_name='CheckID')),
                ('name', models.CharField(max_length=100, verbose_name='Person Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact', models.BigIntegerField(verbose_name='Contact')),
                ('profile', models.URLField(verbose_name='Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PersonalDetails',
        ),
    ]
