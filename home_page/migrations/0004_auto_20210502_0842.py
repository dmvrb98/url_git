# Generated by Django 3.2 on 2021-05-02 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_auto_20210502_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createdurl',
            old_name='c_url',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='usersurl',
            old_name='text',
            new_name='url',
        ),
    ]