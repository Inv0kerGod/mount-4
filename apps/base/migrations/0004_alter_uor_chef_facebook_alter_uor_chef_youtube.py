# Generated by Django 5.0.6 on 2024-06-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_uor_chef_alter_popular_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uor_chef',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook повара'),
        ),
        migrations.AlterField(
            model_name='uor_chef',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='youtube- повара'),
        ),
    ]
