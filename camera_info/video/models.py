from django.db import models
from django.db import models
from django.contrib.auth.models import User

import os

def user_video_upload_path(instance, filename):
    # Get the user's username (assuming it's unique)
    username = instance.uploaded_by.username
    # Generate the path to the user's subfolder
    user_folder = os.path.join('videos', username)
    # Combine the user's subfolder with the uploaded filename
    return os.path.join(user_folder, filename)


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to=user_video_upload_path)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

