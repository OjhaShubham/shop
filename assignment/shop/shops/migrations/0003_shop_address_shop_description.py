# Generated by Django 4.1.7 on 2023-03-29 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_remove_shop_address_alter_shop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
