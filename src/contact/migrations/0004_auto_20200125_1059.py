# Generated by Django 3.0.2 on 2020-01-25 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200125_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinformation',
            old_name='emial',
            new_name='email',
        ),
    ]
