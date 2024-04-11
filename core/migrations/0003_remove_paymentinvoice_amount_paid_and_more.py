# Generated by Django 5.0.3 on 2024-04-11 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_order_bank_remove_order_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentinvoice',
            name='amount_paid',
        ),
        migrations.RemoveField(
            model_name='paymentinvoice',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='core.bank'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
