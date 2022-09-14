from django.db import models
from users.models import User
import uuid

class Options(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class AnswerHistory(models.Model): #for storing the information of users who select an option

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=200, unique=True)
    answer = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question



class PublicOpenion(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appreciate = models.PositiveBigIntegerField(default=0)
    depreciate = models.PositiveBigIntegerField(default=0) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.appreciate


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=200, unique=True)
    option = models.ManyToManyField(Options)
    answer = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="choice")
    public_openion = models.ManyToManyField(PublicOpenion)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question







