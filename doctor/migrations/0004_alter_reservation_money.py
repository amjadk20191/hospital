# Generated by Django 4.1.7 on 2023-06-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_reservation_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Money',
            field=models.BigIntegerField(blank=True, default=0),
        ),
    ]