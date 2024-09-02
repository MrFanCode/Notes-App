from django.db import models

# Create your models here.
class Notes(models.Model):
	title = models.CharField(max_length=255) # Title
	notes = models.TextField() # Notes content
	date_added = models.DateField() # Note's created date