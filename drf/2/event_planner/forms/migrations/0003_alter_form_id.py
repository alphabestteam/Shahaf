# Generated by Django 4.2.4 on 2023-10-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
