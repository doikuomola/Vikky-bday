# Generated by Django 3.2.8 on 2021-10-16 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0006_alter_wish_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
