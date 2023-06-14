# Generated by Django 4.2.1 on 2023-06-14 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_anime_mal_id'),
        ('watchlist', '0010_alter_watchlistanime_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistanime',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.anime'),
        ),
        migrations.AlterUniqueTogether(
            name='watchlistanime',
            unique_together={('watchlist', 'anime')},
        ),
    ]
