# Generated by Django 5.0.6 on 2024-07-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_goodies_goodie'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliateproduct',
            name='name',
            field=models.TextField(default='Unknown Product Name'),
        ),
    ]
