# Generated by Django 4.0.3 on 2022-05-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registerdata',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('access', models.CharField(max_length=100)),
                ('orphanname', models.CharField(max_length=30)),
                ('orphanemail', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('orphanageaddress', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'orphanage_details',
            },
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
