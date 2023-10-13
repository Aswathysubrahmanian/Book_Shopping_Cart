# Generated by Django 4.1 on 2023-10-06 04:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_panel", "0007_alter_order_items"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("name", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: +999999999",
                                regex="^\\+\\d{9}$",
                            )
                        ],
                    ),
                ),
                ("street_address", models.CharField(max_length=255)),
                (
                    "apartment_suite",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("city", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("", "Select a State"),
                            ("ap", "Andhra Pradesh"),
                            ("ar", "Arunachal Pradesh"),
                            ("as", "Assam"),
                            ("br", "Bihar"),
                            ("ch", "Chhattisgarh"),
                            ("ga", "Goa"),
                            ("gj", "Gujarat"),
                            ("hr", "Haryana"),
                            ("hp", "Himachal Pradesh"),
                            ("jh", "Jharkhand"),
                            ("ka", "Karnataka"),
                            ("kl", "Kerala"),
                            ("mp", "Madhya Pradesh"),
                            ("mh", "Maharashtra"),
                            ("mn", "Manipur"),
                            ("ml", "Meghalaya"),
                            ("mz", "Mizoram"),
                            ("nl", "Nagaland"),
                            ("or", "Odisha"),
                            ("pb", "Punjab"),
                            ("rj", "Rajasthan"),
                            ("sk", "Sikkim"),
                            ("tn", "Tamil Nadu"),
                            ("tg", "Telangana"),
                            ("tr", "Tripura"),
                            ("up", "Uttar Pradesh"),
                            ("uk", "Uttarakhand"),
                            ("wb", "West Bengal"),
                            ("an", "Andaman and Nicobar Islands"),
                            ("chd", "Chandigarh"),
                            ("dnh", "Dadra and Nagar Haveli and Daman and Diu"),
                            ("dl", "Delhi"),
                            ("ld", "Lakshadweep"),
                            ("py", "Puducherry"),
                        ],
                        max_length=100,
                    ),
                ),
                ("zip_code", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "billing_address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="billing_address",
                        to="user_panel.address",
                    ),
                ),
                (
                    "shipping_address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shipping_address",
                        to="user_panel.address",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="order", name="billing_address",),
        migrations.RemoveField(model_name="order", name="items",),
        migrations.RemoveField(model_name="order", name="payment",),
        migrations.RemoveField(model_name="order", name="shipping_address",),
        migrations.RemoveField(model_name="order", name="user",),
        migrations.RemoveField(model_name="refund", name="order",),
        migrations.AlterField(
            model_name="user_credentials",
            name="phone_number",
            field=models.CharField(
                max_length=10,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: +999999999",
                        regex="^\\+\\d{9}$",
                    )
                ],
            ),
        ),
        migrations.DeleteModel(name="Billing_Address",),
        migrations.DeleteModel(name="Order",),
        migrations.DeleteModel(name="Payment",),
        migrations.DeleteModel(name="Refund",),
        migrations.AddField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="user_panel.user_credentials",
            ),
        ),
    ]
