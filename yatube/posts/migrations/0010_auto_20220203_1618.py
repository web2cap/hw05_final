# Generated by Django 2.2.6 on 2022-02-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20220203_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(help_text='Укажите ссылку на группу', unique=True, verbose_name='Ссылка на группу'),
        ),
    ]
