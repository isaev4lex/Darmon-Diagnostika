# Generated by Django 3.2.6 on 2021-08-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StomatologyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='media', verbose_name='Картинка')),
                ('description_ru', models.TextField(verbose_name='Содержание (РУС)')),
                ('description_uz', models.TextField(verbose_name='Содержание (УЗБ)')),
            ],
            options={
                'verbose_name': 'Текст для страницы стоматология',
                'verbose_name_plural': 'Текста для страницы стоматология',
            },
        ),
    ]
