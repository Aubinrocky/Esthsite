# Generated by Django 4.0 on 2022-01-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_ca_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]