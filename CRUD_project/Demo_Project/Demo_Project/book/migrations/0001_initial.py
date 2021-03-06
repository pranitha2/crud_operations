# Generated by Django 2.2 on 2022-04-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(default='anonymous', max_length=30)),
                ('rating', models.IntegerField()),
                ('is_bestselling', models.BooleanField(default='False')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
