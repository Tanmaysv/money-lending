# Generated by Django 3.2.7 on 2021-10-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRecord',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cid', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
    ]
