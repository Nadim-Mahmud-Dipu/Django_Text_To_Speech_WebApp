# Generated by Django 3.1.5 on 2021-01-08 15:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_input', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
