# Generated by Django 2.2.6 on 2019-10-15 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_no', models.CharField(max_length=10)),
                ('profile_photo', models.ImageField(blank=True, default='profile/profile_default.png', upload_to='profile')),
                ('cover_photo', models.ImageField(blank=True, default='profile/cover-image/cover_default.jpg', upload_to='profile/cover-image')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_no', models.CharField(max_length=10)),
                ('profile_photo', models.ImageField(blank=True, default='profile/profile_default.png', upload_to='profile')),
                ('cover_photo', models.ImageField(blank=True, default='profile/cover-image/cover_default.jpg', upload_to='profile/cover-image')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
