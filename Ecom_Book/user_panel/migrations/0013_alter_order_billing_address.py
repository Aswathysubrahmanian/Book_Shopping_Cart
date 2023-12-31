# Generated by Django 4.1 on 2023-10-06 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_panel", "0012_order_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="billing_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_panel.address",
            ),
        ),
    ]
