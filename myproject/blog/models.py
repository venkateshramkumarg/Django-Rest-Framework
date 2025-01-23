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
