from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	year = models.PositiveIntegerField(validators=[MinValueValidator(1984), MaxValueValidator(datetime.date.today().year)])
	availability = models.BooleanField(default=True)

	def __str__(self):
		return self.title