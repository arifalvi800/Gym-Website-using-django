# Generated by Django 5.0.6 on 2024-08-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_des', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
