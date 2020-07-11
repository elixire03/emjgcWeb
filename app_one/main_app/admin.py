from django.contrib import admin
from main_app.models import slider, team, service, contact_setting,message, aboutUs
# Register your models here.
admin.site.register(slider)
admin.site.register(team)
admin.site.register(service)
admin.site.register(contact_setting)
admin.site.register(message)
admin.site.register(aboutUs)
