from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length = 30, null = False)
	last_name = models.CharField(max_length = 30, null = True)
	email = models.EmailField()
	password = models.CharField(max_length = 10)
	wallet = models.CharField(max_length=7,null=True)

	def _str_(self):
		return str(self.id)


class Item(models.Model):
	tag = models.CharField(max_length = 30, null = False)
	name = models.CharField(max_length = 30, null = False)

	def _str_(self):
		return str(self.id)
