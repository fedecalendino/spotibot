# Generated by Django 3.1.7 on 2021-03-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("track", "0005_auto_20210305_1406"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="name",
            field=models.TextField(),
        ),
    ]
