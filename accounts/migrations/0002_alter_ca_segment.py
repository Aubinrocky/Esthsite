# Generated by Django 4.0 on 2021-12-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='segment',
            field=models.CharField(choices=[('Soin du visage', 'Soin du visage'), ('Epilation', 'Epilation'), ('Massage', 'Massage'), ('Manucure', 'Manucure')], max_length=200, null=True),
        ),
    ]