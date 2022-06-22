from email.quoprimime import body_check
from optparse import TitledHelpFormatter
from pyexpat import model
from turtle import title
from typing import Text
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post (models.Model):
    title =  models.CharField(max_length=200)
    text = models.TextField
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_Date = models.DateTimeField
    published_Date = models.DateTimeField(auto_now_add=True)
    