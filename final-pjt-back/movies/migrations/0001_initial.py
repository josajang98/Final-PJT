# Generated by Django 3.2.7 on 2022-05-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('overview', models.TextField()),
                ('popularity', models.IntegerField()),
                ('poster_path', models.CharField(max_length=200)),
                ('released_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
