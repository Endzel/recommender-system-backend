# Generated by Django 2.2.2 on 2019-06-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0005_auto_20190623_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Price'),
        ),
    ]