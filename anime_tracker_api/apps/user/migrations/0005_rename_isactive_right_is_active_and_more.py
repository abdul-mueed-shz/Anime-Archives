# Generated by Django 4.2.1 on 2023-06-12 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_right_created_on_alter_right_modified_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='right',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='right',
            old_name='isDeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='isDeleted',
            new_name='is_deleted',
        ),
        migrations.RenameField(
            model_name='userrole',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='userrole',
            old_name='isDeleted',
            new_name='is_deleted',
        ),
    ]