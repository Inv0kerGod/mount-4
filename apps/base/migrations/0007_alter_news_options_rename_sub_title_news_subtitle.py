# Generated by Django 5.0.6 on 2024-07-01 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_news_options_alter_news_sub_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='sub_title',
            new_name='subtitle',
        ),
    ]