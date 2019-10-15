# Generated by Django 2.2.6 on 2019-10-15 10:32

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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=125, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=125, null=True)),
                ('city', models.CharField(choices=[('kathmandu', 'Kathmandu'), ('bhaktapur', 'Bhaktapur'), ('lalitpur', 'Lalitpur')], default='kathmandu', max_length=20)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
