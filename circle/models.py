from django.db import models
# from users.models import User
from sharek.models import Post
import uuid

class Relationship(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fan = models.BooleanField(default=False)
    friend = models.BooleanField(default=False)
    following = models.OneToOneField("users.User", on_delete=models.CASCADE, default=None, null=True, related_name="following")
    follower = models.OneToOneField("users.User", on_delete=models.CASCADE, default=None, null=True, related_name="follower")
    

class Group(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

    GROUP_TYPE_CHOICES= [
        (PRIVATE, "Private"),
        (PUBLIC, "Public"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    group_type = models.CharField(max_length=8, choices=GROUP_TYPE_CHOICES, default="PUBLIC")
    members = models.ManyToManyField("users.User", default=None, related_name="member")
    post = models.ManyToManyField(Post, default=None)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return self.title

