from django.db import models

class AffiliateProduct(models.Model):
    CATEGORY_CHOICES = [
        ('eg', 'Electronic Gadgets'),
        ('ap', 'Apparels'),
        ('hp', 'Health'),
        ('be', 'Beauty'),
        ('hd', 'Home Decor'),
        ('su', 'Subscriptions'),
        ('bo', 'Books'),
        ('co', 'Courses'),
    ]
    
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    name = models.TextField(max_length=150, default='Unknown Product Name')
    detail = models.TextField() 
    image = models.ImageField(upload_to='affiliate_product/')
    link = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.get_category_display()} - {self.detail[:50]}"

class Goodie(models.Model):
    image = models.ImageField(upload_to='goodies/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"
