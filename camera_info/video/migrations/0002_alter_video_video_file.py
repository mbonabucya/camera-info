# Generated by Django 3.2.20 on 2023-10-30 18:27

from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to=video.models.user_video_upload_path),
        ),
    ]