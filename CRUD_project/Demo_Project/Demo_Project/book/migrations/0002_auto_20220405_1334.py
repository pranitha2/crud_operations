# Generated by Django 2.2 on 2022-04-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_bestselling',
            field=models.CharField(max_length=10),
        ),
    ]
