# Generated by Django 3.2.3 on 2021-06-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home_page", "0015_alter_usersurl_url_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersurl",
            name="short",
            field=models.CharField(
                blank=True, error_messages={"unique": ""}, max_length=10, unique=True
            ),
        ),
    ]
