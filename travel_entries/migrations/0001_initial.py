# Generated by Django 3.0 on 2020-08-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=25)),
                ('place_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'TravelEntries',
            },
        ),
    ]
