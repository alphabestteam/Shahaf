# Generated by Django 4.2.4 on 2023-10-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='attack_priority',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='target',
            name='enemy_organization',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='target',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='target',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='target',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='target',
            name='target_goal',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='target',
            name='was_target_destroyed',
            field=models.BooleanField(),
        ),
    ]
