# Generated by Django 4.2.4 on 2023-10-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('target_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
