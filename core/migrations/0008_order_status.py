# Generated by Django 5.0.3 on 2024-04-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_approvedelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('on_progress', 'On Progress'), ('completed', 'Completed')], default='on_progress', max_length=20),
        ),
    ]
