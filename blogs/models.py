from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='blogimages/', default='Image not Found 💀')
    title = models.CharField(max_length=40)
    overview = models.TextField()
    body = models.TextField()

    def __str__(self):
        return f"Title: {self.title}\n Overview: {self.overview}\n Body: {self.body}"
    
