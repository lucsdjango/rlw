from django.db import models
from django.conf import settings
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model


class Experiment(models.Model):
	name = models.CharField(max_length=200)
	instructions = models.TextField(default='instruktioner', max_length=2048)
	welcomeText = models.CharField(default='welcome txt', max_length=200)
	nParticipants = models.IntegerField(default=0)
	def __str__(self):
		return self.name
		
class Condition(models.Model):
	experiment = models.ForeignKey('Experiment', related_name='conditions')
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
		
class Participant(models.Model):
	condition = models.ForeignKey('Condition', related_name='participants')
	age = models.IntegerField(default=0)
	gender = models.CharField(choices=[('male', 'male'), ('female', 'female'), ('-', '-')], default='-', max_length=32)
	hasFinished = models.BooleanField(default=False)
	isExcluded = models.BooleanField(default=False)

class Text(models.Model):
	description = models.CharField(max_length=200,blank=True, default=None, null=True)
	video = models.CharField(max_length=200, blank=True, default=None, null=True,)
	audio = models.CharField(max_length=200, blank=True, default=None, null=True,)

class TextPage(models.Model):
	group = models.ForeignKey('Text', related_name='pages')
	txt = models.TextField(max_length=1024)
	idx = models.IntegerField(default=0)
	startTime = models.FloatField(default=0.0)
	class Meta:
		ordering = ["idx"]
