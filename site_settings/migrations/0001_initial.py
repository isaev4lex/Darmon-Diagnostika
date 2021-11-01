# Generated by Django 3.2.6 on 2021-08-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True, upload_to='media', verbose_name='Favicon')),
            ],
            options={
                'verbose_name': 'Favicon',
                'verbose_name_plural': 'Favicon',
            },
        ),
        migrations.CreateModel(
            name='HeadTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Для чего этот тэг?')),
                ('tag', models.TextField(blank=True, verbose_name='HTML-Код, для <head> элемента')),
            ],
            options={
                'verbose_name': 'Тэг для <head>',
                'verbose_name_plural': 'Тэги для <head>',
            },
        ),
    ]
