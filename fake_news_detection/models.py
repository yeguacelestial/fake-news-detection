from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    CATEGORY_CHOICES = (
        ("BUSINESS", "Business"),
        ("CARS", "Cars"),
        ("ENTERTAINMENT", "Entertainment"),
        ("FAMILY", "Family"),
        ("HEALTH", "Health"),
        ("POLITICS", "Politics"),
        ("RELIGION", "Religion"),
        ("SCIENCE", "Science"),
        ("SPORTS", "Sports"),
        ("TECHNOLOGY", "Technology"),
        ("TRAVEL", "Travel"),
        ("VIDEO", "Video"),
        ("WORLD", "World")
    )

    newspaper = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="POLITICS")
    news_text = models.CharField(max_length=5000)

    def __str__(self):
        return self.news_text