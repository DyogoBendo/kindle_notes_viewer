# Generated by Django 3.2 on 2021-04-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('capa', models.ImageField(upload_to='')),
                ('isbn', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao_inicial', models.IntegerField()),
                ('posicao_final', models.IntegerField()),
                ('destaque', models.TextField()),
                ('data', models.DateTimeField()),
                ('nota', models.TextField()),
            ],
        ),
    ]
