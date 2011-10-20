from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import User
from django_fsm.db.fields import FSMField, transition

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

class Address(models.Model):
  address_line1 = models.CharField("Address line 1", max_length = 256)
  address_line2 = models.CharField("Address line 2", max_length = 256, blank = True)
  postal_code = models.CharField("Postal Code", max_length = 16)
  city = models.CharField(max_length = 256, blank = False)
  state_province = models.CharField("State/Province", max_length = 40, blank = True)
  
  def __unicode__(self):
      return "%s, %s %s" % (self.address_line1, self.city, self.state_province )

class Location(models.Model):
  geolocation =  geomodels.PointField(srid=3857, blank=True, null=True)
  address = models.ForeignKey(Address)
  
class Tree(models.Model):
  location = models.ForeignKey(Location),   
  common_name = models.CharField(max_length=200, blank=True)
  scientific_name = models.CharField(max_length=512, blank=True)
  variety = models.CharField(max_length=512, blank=True)  
  age = models.PositiveIntegerField(default=None, null=True)  
  height = models.DecimalField(max_digits = 5, decimal_places = 2)
  condition = models.PositiveIntegerField(default=None, null=True)  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  status = FSMField(default='unverified', db_index=True)
  stewards = models.ManyToManyField(User, related_name='trees_stewarded_set')
  submitted_by = models.ForeignKey(User, null=True, related_name='submitted_trees_set')
  user_steward_choice = models.CharField(max_length=128, choices=[(x,x) for x in ["yes", "no", "maybe"]])
  
  def __unicode__(self):
    return "%s - %s" % (self.id, self.common_name)
