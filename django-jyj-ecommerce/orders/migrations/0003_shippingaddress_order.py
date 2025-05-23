# Generated by Django 4.2.20 on 2025-04-10 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_shippingaddress"),
    ]

    operations = [
        migrations.AddField(
            model_name="shippingaddress",
            name="order",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.order",
            ),
            preserve_default=False,
        ),
    ]
