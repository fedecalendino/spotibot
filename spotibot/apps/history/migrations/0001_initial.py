# Generated by Django 3.1.7 on 2021-03-04 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("track", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="History",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("uri", models.CharField(max_length=100, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("played_at", models.DateTimeField(unique=True)),
                (
                    "track",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="track.track"
                    ),
                ),
            ],
            options={
                "db_table": "models_history",
            },
        ),
    ]
