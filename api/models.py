from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Breed(models.Model):
    SIZE_OPTIONS = (
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    NUM_OPTIONS = (
        (1, 1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )

    name = models.CharField(max_length=1000)
    size = models.CharField(max_length=10, choices=SIZE_OPTIONS)
    friendliness = models.IntegerField(choices=NUM_OPTIONS)
    trainability = models.IntegerField(choices=NUM_OPTIONS)
    sheddingamount = models.IntegerField(choices=NUM_OPTIONS)
    exerciseneeds = models.IntegerField(choices=NUM_OPTIONS)

    def __str__(self):
        return str(self.name)

class Dog(models.Model):

    name = models.CharField(max_length=1000)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1000)
    color = models.CharField(max_length=1000)
    favoriteFood = models.CharField(max_length=1000)
    favoriteToy = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)
