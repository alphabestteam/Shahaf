# Generated by Django 4.2.4 on 2023-12-14 07:59

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_sum_stars_alter_recipe_avg_starts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='avg_starts',
            field=models.IntegerField(blank=True, editable=False, null=True, validators=[recipes.models.validate_max]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='comments_number',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='sum_stars',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
