from django.db import models

# Create your models here.
class FAQ(models.Model):
	question_body = models.TextField();
	question_answer = models.TextField();
	keywords = models.TextField();

	def __str__(self):
		return (str(self.id) + ": " + str(self.question_body))