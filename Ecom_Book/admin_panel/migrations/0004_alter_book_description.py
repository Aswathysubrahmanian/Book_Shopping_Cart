# Generated by Django 4.1 on 2023-10-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0003_book_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(max_length=800),
        ),
    ]
