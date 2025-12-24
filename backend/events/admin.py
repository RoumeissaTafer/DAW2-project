from django.contrib import admin
#lazem tzidi hadou beh ykhrjou fi admin page normalement
from .models import Event, Session
admin.site.register(Event)
admin.site.register(Session)