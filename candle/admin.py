from django.contrib import admin
from .models import Candle,UploadFile
# Register your models here.

class AdminCandle(admin.ModelAdmin):
    list_display=[field.name for field in Candle._meta.get_fields()]

class AdminUploadFile(admin.ModelAdmin):
    list_display=[field.name for field in UploadFile._meta.get_fields()]

admin.site.register(Candle,AdminCandle)
admin.site.register(UploadFile,AdminUploadFile)