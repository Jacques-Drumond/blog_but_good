# Generated by Django 4.2.1 on 2023-09-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profile_image',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
