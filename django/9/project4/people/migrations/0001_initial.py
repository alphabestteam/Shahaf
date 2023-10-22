# Generated by Django 4.2.4 on 2023-10-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
            ],
        ),
    ]
