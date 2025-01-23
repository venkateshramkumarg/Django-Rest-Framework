from django.db import models
from cuid import cuid

def generate_cuid():
    return cuid()

class Blog(models.Model):
    id=models.CharField(max_length=25,primary_key=True,default=generate_cuid)
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=5000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class User(models.Model):
#     id = models.CharField(max_length=25, primary_key=True, default=generate_cuid)
#     role = models.JSONField(default=default_role)

# class Post(models.Model):
#     id = models.CharField(max_length=25, primary_key=True, default=generate_cuid)
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=5000)
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     liked_by = models.ManyToManyField(User, related_name='liked_posts')
#     disliked_by = models.ManyToManyField(User, related_name='disliked_posts')

# class Comment(models.Model):
#     id = models.CharField(max_length=25, primary_key=True, default=generate_cuid)
#     content = models.CharField(max_length=1000)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')