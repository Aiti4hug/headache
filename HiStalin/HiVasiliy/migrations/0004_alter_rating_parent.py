# Generated by Django 5.1.4 on 2024-12-12 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiVasiliy', '0003_rating_parent_alter_movielanguages_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='HiVasiliy.rating'),
        ),
    ]