# Generated by Django 4.2.1 on 2023-06-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_right_role_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='right',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
