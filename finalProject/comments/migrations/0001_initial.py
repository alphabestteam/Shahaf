# Generated by Django 4.2.4 on 2023-12-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('text', models.TextField()),
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
