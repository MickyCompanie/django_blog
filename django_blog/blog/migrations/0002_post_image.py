# Generated by Django 3.1.5 on 2021-02-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_post.png', upload_to='posts_pics'),
        ),
    ]