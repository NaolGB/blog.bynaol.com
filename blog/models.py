from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    content = models.TextField()
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    written_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog_blog", kwargs={"slug": self.slug})