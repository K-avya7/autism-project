# Generated by Django 5.1.1 on 2024-10-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_donate_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('program_participation', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('address', models.TextField()),
            ],
        ),
    ]
