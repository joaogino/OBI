from django.contrib import admin
from .models import Videoaula
# Register your models here.
class VideoaulaAdmin(admin.ModelAdmin):
    list_display = ["ano", "fase","nivel","titulo"]

# Register the admin class with the associated model
admin.site.register(Videoaula, VideoaulaAdmin)