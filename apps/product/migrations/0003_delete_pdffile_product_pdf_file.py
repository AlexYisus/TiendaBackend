# Generated by Django 5.0.4 on 2024-12-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_pdffile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PDFFile',
        ),
        migrations.AddField(
            model_name='product',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/%Y/%m/'),
        ),
    ]
