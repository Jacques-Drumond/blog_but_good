from django.db import models
from PIL import Image
# Create your models here.
class BlogPost(models.Model):
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='blog/images/')
    author = models.CharField(max_length=100)
    date = models.DateField()
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title