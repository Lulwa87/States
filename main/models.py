from django.db import models

# Create your models here.
class State(models.Model):
	abbreviation = models.CharField(max_length=2, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	
	def __unicode__(self):
		return "%s" % self.name



class StateCapital(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	state = models.OneToOneField('main.State', null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	capital_population = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return "%s" % self.name

class City(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	county = models.CharField(max_length=100, null=True, blank=True)
	state = models.ForeignKey("main.State", null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	zip_code = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return "%s" % self.name

