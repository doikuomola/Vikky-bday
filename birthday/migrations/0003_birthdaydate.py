# Generated by Django 3.2.8 on 2021-10-16 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_image_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdayDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'BirthdayDate',
                'verbose_name_plural': 'BirthdayDates',
            },
        ),
    ]
