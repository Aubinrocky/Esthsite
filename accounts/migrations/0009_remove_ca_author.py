# Generated by Django 4.0 on 2021-12-30 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_ca_client_ca_author_delete_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ca',
            name='author',
        ),
    ]
