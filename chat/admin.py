from django.contrib import admin

# Register your models here.
from .models import Human, Room, Message

admin.site.register(Human)
admin.site.register(Room)

admin.site.register(Message)
