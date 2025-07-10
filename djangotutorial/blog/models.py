from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.name} age ({self.age_now} yrs)"
    
    @property
    def age_now(self):
        today = timezone.localdate()
        return today.year - self.date_of_birth.year - (
        (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
    )


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.title


