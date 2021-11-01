# Generated by Django 3.0 on 2021-08-08 23:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('players', models.CharField(max_length=100)),
                ('bowlers', models.IntegerField()),
                ('batsman', models.IntegerField()),
                ('wicketkeeper', models.IntegerField()),
                ('coach', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]