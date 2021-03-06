# Generated by Django 3.1.7 on 2021-04-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210327_0815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'галерею', 'verbose_name_plural': 'галерея'},
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='text',
        ),
        migrations.AlterField(
            model_name='room',
            name='features',
            field=models.CharField(help_text='Например - беспроводной интернет и телевизор', max_length=100, verbose_name='Особенности'),
        ),
        migrations.AlterField(
            model_name='room',
            name='short_description',
            field=models.CharField(help_text='Будет показано на карточке номера', max_length=150, verbose_name='Краткое описание'),
        ),
    ]
