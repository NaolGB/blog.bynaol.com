from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    written_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title