# Generated by Django 5.0.3 on 2024-04-11 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_paymentinvoice_bank_order_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
    ]
