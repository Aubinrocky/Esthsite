# Generated by Django 4.0 on 2021-12-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_ca_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
