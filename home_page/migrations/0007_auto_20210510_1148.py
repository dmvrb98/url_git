# Generated by Django 3.2 on 2021-05-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_auto_20210502_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurl',
            name='text',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='CreatedUrl',
        ),
    ]
