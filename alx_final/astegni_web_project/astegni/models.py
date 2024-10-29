import uuid 
from django.db import models
from django.utils import timezone

"""Comment about the file"""

class Tutor(models.Model):
  """Turor Model To Handle Users Register as a Tutor."""
  tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(max_length=20)
  middle_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  gender = models.CharField(max_length=5)
  age = models.IntegerField()
  email = models.CharField(max_length=30)
  Tel_number = models.CharField(max_length=15)
  location =  models.CharField(max_lenght=15)
  tutor_registeration_date = models.DateTimeField(default=timezone.now)

class Parent(models.Model):
  """Parent Model To Handle Users Register as a Parent."""
  parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(max_length=20)
  middle_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  gender = models.CharField(max_length=5)
  age = models.IntegerField()
  email = models.CharField(max_length=30)
  Tel_number = models.CharField(max_length=15)
  location =  models.CharField(max_lenght=15)
  parent_registeration_date = models.DateTimeField(default=timezone.now)

class Review(models.Model):
  """Review Model To Handle Parent Review on a Specific Tutor."""
  comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  comment = models.TextField(max_length=1024)
  rating = models.
  review_date = models.DateTimeField(default=timezone.now)

class Subject(models.Model):
  """Subject Model To Handle Subject Information Given By Tutors."""
  title_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=15)

class Schedule(models.Model): 
  """Schedule Model To Hanlde Tutor Schedule between Specific Tutor and Parent."""
  schedule_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  schedule_created_at = models.DateTimeField(default=timezone.now)
