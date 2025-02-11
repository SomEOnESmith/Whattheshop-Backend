# Generated by Django 2.2.6 on 2019-10-21 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='transactionitem',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencyitem', to='api.Crypto'),
        ),
    ]
