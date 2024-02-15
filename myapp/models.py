from django.db import models

class myModel(models.Model):
	end_year = models.PositiveIntegerField(null=True, blank=True)
	intensity = models.PositiveSmallIntegerField(null=True, blank=True)
	sector = models.CharField(max_length = 255, null=True, blank=True)
	topic = models.CharField(max_length = 55, null=True, blank=True)
	insight = models.TextField()
	url = models.URLField(max_length = 300)
	region = models.CharField(max_length = 50, null=True, blank=True)
	start_year = models.PositiveIntegerField(null=True, blank=True)
	impact = models.CharField(max_length = 255, null=True, blank=True)
	added = models.DateTimeField(null=True, blank=True)
	published = models.DateTimeField(null=True, blank=True)
	country = models.CharField(max_length = 50, null=True, blank=True)
	relevance = models.PositiveIntegerField(null=True, blank=True)
	pestle = models.CharField(max_length = 100, null=True, blank=True)
	source = models.CharField(max_length = 200, null=True, blank=True)
	title = models.CharField(max_length = 300, null=True, blank=True)
	likelihood = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return self.insight