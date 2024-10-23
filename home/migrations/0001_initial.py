# Generated by Django 5.1.1 on 2024-10-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
