# Generated by Django 4.2.1 on 2023-06-12 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0004_alter_watchlist_created_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='isDeleted',
            new_name='is_deleted',
        ),
    ]
