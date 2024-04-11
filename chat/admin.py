from django.contrib import admin
from .models import ChatGroup, Message, Profile

admin.site.register([ChatGroup, Message, Profile])
