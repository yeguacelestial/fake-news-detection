from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    CATEGORY_CHOICES = (
        ("Business", "Business"),
        ("Cars", "Cars"),
        ("Entertainment", "Entertainment"),
        ("Family", "Family"),
        ("Health", "Health"),
        ("Politics", "Politics"),
        ("Religion", "Religion"),
        ("Science", "Science"),
        ("Sports", "Sports"),
        ("Technology", "Technology"),
        ("Travel", "Travel"),
        ("Video", "Video"),
        ("World", "World")
    )

    newspaper = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="Politics")
    news_text = models.CharField(max_length=5000)
    label = models.CharField(max_length=10, default="Fake")

    def __str__(self):
        return self.news_text