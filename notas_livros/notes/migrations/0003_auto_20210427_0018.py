# Generated by Django 3.2 on 2021-04-27 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210426_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='capa',
            field=models.ImageField(upload_to='book_cover/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='data',
            field=models.CharField(max_length=200),
        ),
    ]