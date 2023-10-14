from django.db import models
from common.models import BaseModelWithUid

# Create your models here.
class User(BaseModelWithUid):
    name = models.CharField(max_length=50)
    
