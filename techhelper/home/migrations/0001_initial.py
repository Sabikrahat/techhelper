# Generated by Django 3.2.4 on 2021-08-25 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messengerId', models.CharField(max_length=10)),
                ('messengerUsername', models.CharField(max_length=30)),
                ('messengerEmail', models.CharField(max_length=50)),
                ('messengerPhoneNumber', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=3072)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users_contacts',
            },
        ),
        migrations.CreateModel(
            name='UserInternships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisherId', models.CharField(max_length=15)),
                ('publisherName', models.CharField(max_length=50)),
                ('internshipTitle', models.CharField(max_length=20)),
                ('companyName', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=3072)),
                ('internshipType', models.CharField(max_length=15)),
                ('paymentStatus', models.CharField(max_length=15)),
                ('workPlace', models.CharField(max_length=15)),
                ('minSalary', models.CharField(max_length=15)),
                ('maxSalary', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users_internships',
            },
        ),
        migrations.CreateModel(
            name='UserJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisherId', models.CharField(max_length=15)),
                ('publisherName', models.CharField(max_length=50)),
                ('jobTitle', models.CharField(max_length=20)),
                ('companyName', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=3072)),
                ('jobType', models.CharField(max_length=15)),
                ('paymentStatus', models.CharField(max_length=15)),
                ('workPlace', models.CharField(max_length=15)),
                ('minSalary', models.CharField(max_length=15)),
                ('maxSalary', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users_jobs',
            },
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisherId', models.CharField(max_length=20)),
                ('publisherName', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3072)),
                ('type', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=3072)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users_questions',
            },
        ),
    ]
