# Generated by Django 3.1.5 on 2021-02-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_post.jpg', upload_to='posts_pics'),
        ),
    ]
