# Generated by Django 3.1.5 on 2021-01-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hole', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='email',
            field=models.EmailField(max_length=191, primary_key=True, serialize=False),
        ),
    ]