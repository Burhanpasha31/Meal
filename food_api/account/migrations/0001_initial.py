# Generated by Django 5.0 on 2023-12-18 13:59

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='user_image')),
                ('email_verified', models.BooleanField(default=False)),
                ('phone_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='is_seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='is_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('cost', models.IntegerField()),
                ('phone', models.CharField(default='', max_length=15)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.is_seller')),
            ],
        ),
    ]
