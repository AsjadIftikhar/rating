# Generated by Django 4.0.2 on 2022-03-25 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_pdfbook_remove_book_pdf_book_asin_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
