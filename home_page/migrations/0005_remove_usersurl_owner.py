# Generated by Django 3.2 on 2021-05-02 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home_page", "0004_auto_20210502_0842"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersurl",
            name="owner",
        ),
    ]
