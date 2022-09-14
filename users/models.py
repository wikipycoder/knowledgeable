from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# from wallet.models import DigitalWallet

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    post = models.ManyToManyField("sharek.Post", related_name="post")
    relationship = models.ManyToManyField("circle.Relationship")
    # # wallet = models.OneToOneField(DigitalWallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.username







