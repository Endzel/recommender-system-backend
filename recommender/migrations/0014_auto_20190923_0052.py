# Generated by Django 2.2.2 on 2019-09-23 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0013_remove_item_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gps_point',
            field=models.TextField(blank=True, verbose_name='GPS Point'),
        ),
    ]
