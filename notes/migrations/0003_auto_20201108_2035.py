# Generated by Django 3.1.3 on 2020-11-08 20:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20201011_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
