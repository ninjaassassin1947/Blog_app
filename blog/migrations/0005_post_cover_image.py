# Generated by Django 5.0.7 on 2024-08-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='files/covers'),
        ),
    ]
