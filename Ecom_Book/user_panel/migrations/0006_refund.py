# Generated by Django 4.1 on 2023-10-05 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_panel", "0005_rename_billingaddress_billing_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Refund",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reason", models.TextField()),
                ("accepted", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_panel.order",
                    ),
                ),
            ],
        ),
    ]
