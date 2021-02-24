from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default_post.jpg', upload_to='posts_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 900 or img.width > 900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.image.path)