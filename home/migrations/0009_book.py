# Generated by Django 4.0.2 on 2022-03-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ASIN', models.CharField(max_length=255, null=True, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255, null=True)),
                ('total_words', models.IntegerField(null=True)),
                ('profane_percentage', models.FloatField(null=True)),
                ('customer_history', models.ManyToManyField(blank=True, related_name='books', to='home.CustomerHistory')),
            ],
        ),
    ]