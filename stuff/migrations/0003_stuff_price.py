# Generated by Django 2.2.4 on 2019-08-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0002_stuff_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
