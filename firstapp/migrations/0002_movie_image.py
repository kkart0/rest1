# Generated by Django 4.1.4 on 2023-04-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
