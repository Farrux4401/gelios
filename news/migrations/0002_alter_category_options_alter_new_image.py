# Generated by Django 4.1.7 on 2023-02-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
