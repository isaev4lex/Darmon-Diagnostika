# Generated by Django 3.2.6 on 2021-08-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20210824_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emails',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='phonenumbers',
            name='number',
            field=models.CharField(max_length=18, verbose_name='Номер'),
        ),
    ]
