# Generated by Django 4.2.11 on 2024-12-13 17:18

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomManagerModel",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(default="test data", max_length=50)),
                ("deleted", models.BooleanField(default=False)),
            ],
            managers=[
                ("all_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]