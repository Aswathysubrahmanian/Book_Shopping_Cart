# Generated by Django 4.1 on 2023-10-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_panel", "0011_remove_order_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="image",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]