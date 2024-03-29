# Generated by Django 4.2.1 on 2023-06-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('mal_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'anime',
            },
        ),
    ]
