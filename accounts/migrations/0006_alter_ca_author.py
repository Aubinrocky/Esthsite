# Generated by Django 4.0 on 2021-12-29 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0005_alter_ca_segment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
