import uuid 
from typing import List
from django.db import models
from django.utils import timezone


class Person(models.Model):
  """This class act as a base class for Parent and Tutor class's."""
  # Options to fill in gender filed 
  GENDER = [('Male', 'Male'), ('Female', 'Female'),]
  first_name:str = models.CharField(max_length=20)
  middle_name:str= models.CharField(max_length=20)
  last_name:str= models.CharField(max_length=20)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_new=True)
  gender:str = models.CharField(max_length=5, null=False, choices=GENDER)
  age:int= models.IntegerField(null=True)
  email:str = models.CharField(max_length=30, unique=True, null=False)
  password:str = models.CharField(max_length=30, null=False)
  Tel_number:str = models.CharField(max_length=15, null=False)
  location:str =  models.CharField(max_length=15, null=False)

  class Meta:
        abstract = True

class Tutor(Person):
  """Turor Model To Handle Users Register as a Tutor."""
  tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  profile_image = models
  description:str = models.TextField(max_length=2000)

  available_days:List = # put relationship with schedule model
  subject_interst:List = # Put relationship with subject model

  
 
class Parent(Person):
  """Parent Model To Handle Users Register as a Parent."""
  parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  # a Tutor can serve 1 or many parents at a time.
  # a parent served by a single Tutor at a time.
  # 'parents' refer current parents associated with a tutor.
  tutor = models.ForeignKey(Tutor, related_name='parents', on_delete=models.CASCADE )


class Subject(models.Model):
  """Subject Model To Handle Subject Information Given By Tutors."""
  title_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
  title = models.CharField(max_length=15)

 
class Schedule(models.Model): 
  """Schedule Model To Hanlde Tutor Schedule between Specific Tutor and Parent."""
  schedule_id: str = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  schedule_created_at: str = models.DateTimeField(default=timezone.now)
  schedule_updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
  """Review Model To Handle Parent Review on a Specific Tutor."""
  review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  review_created_at = models.DateTimeField(default=timezone.now)
  review_updated_at = models.DateTimeField(auto_now=True)

  review_message = models.TextField(max_length=1024)
  tutor_rating = models.IntegerField()

  # Relationship with 1 parent and 1 tutor id 2 FKeys.


class Feedback(models.Model): # Done
  """Feeback Model To Handle Tutor's and Parent's Feedback of the Service."""
  feedback_id: str = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  feedback_created_at = models.DateTimeField(default=timezone.now)
  feedback_updated_at = models.DateTimeField(auto_now=True)

  feedback_message: str = models.TextField(max_length=2000)

  # Relationship with 1 parent or 1 tutor id who give the feedback Fkey.

class Report(models.Model): #Done
  """Report Model To Handle Tutor's and Parent's Report's."""
  report_id: str = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  report_created_at = models.DateTimeField(default=timezone.now)
  report_updated_at = models.DateTimeField(auto_now=True)

  report_title = models.TextField(max_length=100)
  report_message: str = models.TextField(max_length=2000)

  # Relationship with 1 parent and 1 tutor id 2 Fkeys.
  # A parent can submit a report on a tutor.
  # A tutor can submit a report on a parent.

class ParentPayment(models.Model):
    """Payment Model To Handle Payments Made by Parents."""
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_created_at = models.DateTimeField(default=timezone.now)
    payment_updated_at = models.DateTimeField(auto_now=True)
    payment_amount = models.IntegerField()
    payment_reason = models.TextField()


class TutorPayment(models.Model):
    """Payment Model To Handle Payments Made To Tutors."""

    # Payment status 
    STATUS = [('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed'),]

    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_created_at = models.DateTimeField(default=timezone.now)
    payment_updated_at = models.DateTimeField(auto_now=True)
    payment_amount = models.IntegerField()
    payment_reason = models.TextField() 
    payment_status = models.CharField(max_length=15, choices=STATUS)

    # Multiple payments can be made for a tutor.
    # 'Payments' refer payments made for a tutor.
    tutor_payment = models.ForeignKey(Tutor, related_name='payments', on_delete=models.CASCADE)

    