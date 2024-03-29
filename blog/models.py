from django.db import models
from PIL import Image
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    formation = models.CharField(max_length=100, null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=200, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    profile_image = models.ImageField(upload_to ='posts', default="Default_pfp.svg.png")   
    user_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    comment = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    rating = models.IntegerField(default=1, null=False, blank=False, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
        ])

    def __str__(self):
        return f"{self.user_name}"
    
    