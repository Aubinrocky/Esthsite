# Generated by Django 4.0 on 2022-01-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_ca_month_alter_ca_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='year',
            field=models.CharField(choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=200, null=True),
        ),
    ]