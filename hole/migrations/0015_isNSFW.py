# Generated by Django 3.2 on 2021-04-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hole', '0014_auto_20210416_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='is_NSFW',
            field=models.BooleanField(default=False),
        ),
    ]