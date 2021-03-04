# Generated by Django 3.1.7 on 2021-03-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="history",
            name="raw",
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="history",
            name="id",
            field=models.CharField(
                default="21be52ab-30b8-44f1-8a22-1606386474ba",
                max_length=100,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
