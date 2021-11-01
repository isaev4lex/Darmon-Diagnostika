# Generated by Django 3.2.6 on 2021-08-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GastroenterologistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=300, unique=True, verbose_name='Название (РУС)')),
                ('description_ru', models.TextField(verbose_name='Описание (РУС)')),
                ('title_uz', models.CharField(max_length=300, unique=True, verbose_name='Название (УЗБ)')),
                ('description_uz', models.TextField(verbose_name='Описание (УЗБ)')),
                ('slug', models.CharField(blank=True, max_length=300, unique=True, verbose_name='URL (Необязательно)')),
            ],
            options={
                'verbose_name': 'Информацию для страницы гастроэнторолог',
                'verbose_name_plural': 'Информация для страницы гастроэнторолог',
            },
        ),
    ]
