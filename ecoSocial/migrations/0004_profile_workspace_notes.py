# Generated by Django 5.2.3 on 2025-07-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecoSocial", "0003_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="workspace_notes",
            field=models.TextField(blank=True, default=""),
        ),
    ]
