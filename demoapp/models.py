from django.db import models

class assignments(models.Model):
	heading = models.CharField(max_length = 30)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.heading

class submission(models.Model):
	title = models.CharField(max_length = 30)
	description = models.TextField()
	assignment = models.ForeignKey(assignments, on_delete = models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title