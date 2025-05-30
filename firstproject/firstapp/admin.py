from django.contrib import admin
from .models import Reservation  # ✅ Corrected

# Register your models here.

admin.site.register(Reservation)
