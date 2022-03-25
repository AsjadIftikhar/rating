# Generated by Django 4.0.2 on 2022-03-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_books_history_books_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='history',
        ),
        migrations.AddField(
            model_name='books',
            name='customer_history',
            field=models.ManyToManyField(blank=True, related_name='books', to='home.CustomerHistory'),
        ),
        migrations.AddField(
            model_name='books',
            name='profane_percentage',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='profane_words',
            field=models.FloatField(null=True),
        ),
    ]
