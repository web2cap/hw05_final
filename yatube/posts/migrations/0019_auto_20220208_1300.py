# Generated by Django 2.2.16 on 2022-02-08 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20220208_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
    ]
