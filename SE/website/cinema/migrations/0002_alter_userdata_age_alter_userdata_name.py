# Generated by Django 4.2.1 on 2023-06-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
