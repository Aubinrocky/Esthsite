# Generated by Django 4.0 on 2022-01-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_profile_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]