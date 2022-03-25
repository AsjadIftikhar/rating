# Generated by Django 4.0.2 on 2022-03-24 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ASIN', models.CharField(max_length=255, null=True, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255, null=True)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.history')),
            ],
        ),
    ]