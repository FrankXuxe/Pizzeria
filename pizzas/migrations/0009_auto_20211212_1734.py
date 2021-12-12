# Generated by Django 3.0.5 on 2021-12-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0008_image_piz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]