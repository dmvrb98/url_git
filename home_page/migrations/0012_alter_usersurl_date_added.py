# Generated by Django 3.2.3 on 2021-05-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0011_auto_20210525_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurl',
            name='date_added',
            field=models.DateTimeField(null=True),
        ),
    ]
