# Generated by Django 3.2.8 on 2021-10-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0004_wish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'verbose_name': 'Wish', 'verbose_name_plural': 'Wishes'},
        ),
        migrations.AlterField(
            model_name='wish',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
