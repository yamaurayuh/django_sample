# Generated by Django 4.2.4 on 2023-08-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchandiseID', models.CharField(max_length=6)),
                ('merchandise', models.CharField(max_length=10)),
                ('unitPrice', models.IntegerField()),
            ],
        ),
    ]
