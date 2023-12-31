# Generated by Django 4.0.5 on 2023-09-13 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999', regex='^\\+?1?\\d{9,15}$')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('password', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
    ]
