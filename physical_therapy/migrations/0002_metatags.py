# Generated by Django 3.2.6 on 2021-08-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physical_therapy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('keywords', models.TextField(verbose_name='Keywords (Через запятую/Предложением)')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Мета тег',
                'verbose_name_plural': 'Мета теги',
            },
        ),
    ]
