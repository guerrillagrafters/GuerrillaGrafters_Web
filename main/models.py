from django.db import models
from django.contrib.auth.models import User
from django_fsm.db.fields import FSMField, transition

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    
class Tree(models.Model):
  location = models.PointField(srid=3857)
  common_name = models.CharField(max_length = 100)
  scientific_name = models.CharField(max_length = 100)
  native_to = models.CharField(max_length = 100)
  species = models.CharField(max_length = 100)
  variety = models.CharField(max_length = 100)
  span = models.DecimalField(max_digits = 5, decimal_places = 2)
  height = models.DecimalField(max_digits = 5, decimal_places = 2)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  status = FSMField(default='unverified', db_index=True)

  def __unicode__(self):
    return self.common_name
