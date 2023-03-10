# Generated by Django 2.2.28 on 2022-12-10 11:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=245, unique=True)),
                ('photo', models.ImageField(upload_to='services/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
