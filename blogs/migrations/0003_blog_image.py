# Generated by Django 5.0.6 on 2024-07-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_blogs_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='Image not Found 💀', upload_to='blogimages/'),
        ),
    ]
