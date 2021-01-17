# Generated by Django 3.1.5 on 2021-01-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.IntegerField(max_length=10)),
                ('password2', models.IntegerField(max_length=10)),
            ],
        ),
    ]
