# Generated by Django 3.0.5 on 2020-04-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=16, null=True),
        ),
    ]
