from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class ChatGroup(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    chat_group = models.ForeignKey(ChatGroup, models.CASCADE)
    sender = models.ForeignKey(User, models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    status = models.CharField(default="offline", max_length=100)
    image = models.ImageField(upload_to="profile_images/", default="default.jpg")

    def __str__(self):
        return f"Profile of {self.user.username}"


@receiver(sender=User, signal=post_save)
def create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

