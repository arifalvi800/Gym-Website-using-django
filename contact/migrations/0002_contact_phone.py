# Generated by Django 5.1.1 on 2024-09-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="phone",
            field=models.CharField(default="", max_length=15),
        ),
    ]
