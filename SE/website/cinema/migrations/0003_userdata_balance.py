# Generated by Django 4.2.1 on 2023-06-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_alter_userdata_age_alter_userdata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
