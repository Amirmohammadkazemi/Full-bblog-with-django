# Generated by Django 4.0 on 2021-12-19 08:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_media_mediaaddress_alter_header_headerdescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='MediaPage',
            field=models.CharField(max_length=100, null=True, verbose_name='لینک صفحه'),
        ),
        migrations.AlterField(
            model_name='media',
            name='MediaBody',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Body', null=True, verbose_name='متن'),
        ),
    ]