# Generated by Django 3.0.2 on 2020-01-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=15)),
                ('emial', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]