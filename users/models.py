from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
from cloudinary import uploader


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField(
        "avatar",
        default="https://res.cloudinary.com/dvex4uzyg/image/upload/fl_preserve_transparency/v1727104361/CulinaryHub/default_avatar_l48hpr.jpg",
    )

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if self.avatar and hasattr(self.avatar, "url"):
    #         # Resize image in Cloudinary
    #         uploader.upload(
    #             self.avatar.url,
    #             public_id=self.avatar.public_id,
    #             overwrite=True,
    #             transformation=[{"width": 250, "height": 250, "crop": "limit"}],
    #         )
