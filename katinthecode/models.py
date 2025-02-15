"""This is the models file for the katinthecode app."""

from django.db import models


class Post(models.Model):
    """This is the Post model for the katinthecode app."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    post_text = models.TextField(max_length=80000)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # Add default manager


class Post_Tag(models.Model):
    """This is the Post_Tag model for the katinthecode app."""

    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Post_Image(models.Model):
    """This is the Post_Image model for the katinthecode app."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    img = models.ImageField(upload_to="images/", default=None)
    description = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
