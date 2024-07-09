from django.contrib import admin
from .models import Train, Reservation, Payment

admin.site.register(Train)
admin.site.register(Reservation)
admin.site.register(Payment)
