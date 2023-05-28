# Generated by Django 4.1.7 on 2023-05-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]