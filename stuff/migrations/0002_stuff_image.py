# Generated by Django 2.2.4 on 2019-08-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/stuff_image/'),
        ),
    ]