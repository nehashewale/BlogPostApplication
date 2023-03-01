from django.db import models
from uuid import uuid4


class User(models.Model):
    username = models.CharField(max_length=30, unique=True, db_index=True,default="")
    name = models.CharField(max_length=50,default="")
    created_time = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    

class Like(models.Model):
    uuid = models.CharField(max_length=255,default=uuid4)
    post_uuid = models.CharField(max_length=255) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField('Created Time', auto_now_add=True, null=True)

class Post(models.Model):
    PUBLIC="PUBLIC"
    PRIVATE="PRIVATE"
    access_type_choices = (
        (PRIVATE,'PRIVATE'),
        (PUBLIC,'PUBLIC'),
    )
    uuid = models.CharField(max_length=255,default=uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)  # identify user's POST
    content = models.CharField(max_length=255) # content of POST 
    likes =  models.ManyToManyField(Like)   # mapping of like count
    access_type = models.CharField(max_length=64, choices=access_type_choices) # access type either private or public
    created_time = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    archived = models.BooleanField(default=False)