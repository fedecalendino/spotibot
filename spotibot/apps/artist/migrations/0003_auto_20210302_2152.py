# Generated by Django 3.1.7 on 2021-03-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20210302_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
