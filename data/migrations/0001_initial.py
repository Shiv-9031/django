# Generated by Django 4.1.10 on 2023-08-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('end_year', models.IntegerField()),
                ('intensity', models.IntegerField()),
                ('relevance', models.IntegerField()),
                ('likelihood', models.IntegerField()),
                ('sector', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('insight', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
                ('published', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pestle', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
