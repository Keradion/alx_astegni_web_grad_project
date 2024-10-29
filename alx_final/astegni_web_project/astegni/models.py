import uuid 
from typing import List
from django.db import models
from django.utils import timezone

"""Comment about the file"""

class Tutor(models.Model):
  """Turor Model To Handle Users Register as a Tutor."""
  tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  first_name:str = models.CharField(max_length=20)
  middle_name:str= models.CharField(max_length=20)
  last_name:str= models.CharField(max_length=20)
  gender:str = models.CharField(max_length=5)
  age:int= models.IntegerField()

  email:str = models.CharField(max_length=30)
  password:str = models.CharField(max_length=30)
  Tel_number:str = models.CharField(max_length=15)
  location:str =  models.CharField(max_lenght=15)
  tutor_registeration_date = models.DateTimeField(default=timezone.now)


  profile_image = models
  description:str = models.TextField(max_length=2000)

  available_days:List = # put relationship with schedule model
  subject_interst:List = # Put relationship with subject model

class Parent(models.Model):
  """Parent Model To Handle Users Register as a Parent."""
  parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  first_name = models.CharField(max_length=20)
  middle_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  gender = models.CharField(max_length=5)
  age = models.IntegerField()

  email = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  Tel_number = models.CharField(max_length=15)
  location =  models.CharField(max_lenght=15)

  parent_registeration_date = models.DateTimeField(default=timezone.now)


class Subject(models.Model):
  """Subject Model To Handle Subject Information Given By Tutors."""
  title_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=15)
 
class Schedule(models.Model): 
  """Schedule Model To Hanlde Tutor Schedule between Specific Tutor and Parent."""
  schedule_id: str = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  schedule_created_at: str = models.DateTimeField(default=timezone.now)

class Review(models.Model):
  """Review Model To Handle Parent Review on a Specific Tutor."""
  review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  review_created_at = models.DateTimeField(default=timezone.now)
  review_updated_at = models.DateTimeField(default=timezone.now)

  review_message = models.TextField(max_length=1024)
  tutor_rating = models.IntegerField()

  # Relationship with 1 parent and 1 tutor id 2 FKeys.

class Feedback(models.Model): # Done
  """Feeback Model To Handle Tutor's and Parent's Feedback of the Service."""
  feedback_id: str = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  feedback_created_at = models.DateTimeField(default=timezone.now)
  feedback_updated_at = models.DateTimeField(default=timezone.now)

  feedback_message: str = models.TextField(max_length=2000)

  # Relationship with 1 parent or 1 tutor id who give the feedback Fkey.

class Report(models.Modle): #Done
  """Report Model To Handle Tutor's and Parent's Report's."""
  report_id: str = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  report_created_at = models.DateTimeField(default=timezone.now)
  report_updated_at = models.DateTimeField(default=timezone.now)

  report_title = models.TextField(max_length=100)
  report_message: str = models.TextField(max_length=2000)

  # Relationship with 1 parent and 1 tutor id 2 Fkeys.
  # A parent can submit a report on a tutor.
  # A tutor can submit a report on a parent.