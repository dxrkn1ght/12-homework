from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('1', 'Elektronika'),
        ('2', 'Kiyim-kechak'),
        ('3', 'Oziq-ovqat'),
        ('4', 'Uy-ro\'zg\'or buyumlari'),
    ]

    title = models.CharField(max_length=255)
    short_content = models.TextField()
    long_content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
