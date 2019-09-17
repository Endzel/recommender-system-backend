# Generated by Django 2.2.2 on 2019-09-17 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0009_auto_20190917_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='context_segment',
        ),
        migrations.CreateModel(
            name='RecommendationContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Weight')),
                ('context_segment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group_contexts', to='recommender.ContextSegment', verbose_name='Context segment')),
            ],
        ),
        migrations.AddField(
            model_name='recommendation',
            name='context',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommender.RecommendationContext', verbose_name='Context'),
            preserve_default=False,
        ),
    ]