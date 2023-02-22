from django.db import models

# Create your models here.
class Candle(models.Model):
    name = models.CharField(max_length=70)
    #date = models.DateField()
    date = models.IntegerField()
    time = models.TimeField()
    open = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    close = models.FloatField(default=0.0)
    volume = models.IntegerField(default=0)
    
class UploadFile(models.Model):
    csv_file =models.FileField(upload_to='candle')
    timeframe= models.IntegerField()