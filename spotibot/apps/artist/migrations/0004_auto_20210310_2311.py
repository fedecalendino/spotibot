# Generated by Django 3.1.7 on 2021-03-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artist", "0003_auto_20210302_2152"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="name",
            field=models.TextField(),
        ),
    ]
