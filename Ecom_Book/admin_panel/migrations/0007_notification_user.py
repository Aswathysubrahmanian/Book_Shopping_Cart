# Generated by Django 4.1 on 2023-10-08 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admin_panel", "0006_rename_timestamp_notification_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                default=1234,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]