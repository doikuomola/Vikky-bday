# Generated by Django 3.2.8 on 2021-10-16 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0007_wish_createat'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
