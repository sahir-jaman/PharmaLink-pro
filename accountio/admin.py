from django.contrib import admin
from .models import User

# Register your models here.



# Now register the new UserModelAdmin...
admin.site.register(User)