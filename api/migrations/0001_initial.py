# Generated by Django 3.2.9 on 2022-04-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('jobs', models.IntegerField()),
                ('coins', models.IntegerField()),
            ],
        ),
    ]
