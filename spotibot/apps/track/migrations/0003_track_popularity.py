# Generated by Django 3.1.7 on 2021-03-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("track", "0002_auto_20210304_1241"),
    ]

    operations = [
        migrations.AddField(
            model_name="track",
            name="popularity",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
