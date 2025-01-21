from django.db import models

# Create your models here.


class ContactMe(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	message = models.TextField()

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Contact Me'
		
	def __str__(self):
		return self.name