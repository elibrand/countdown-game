# Generated by Django 3.0.1 on 2019-12-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20191228_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(max_length=100),
        ),
    ]
