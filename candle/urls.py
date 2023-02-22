from django.urls import path, include
from candle import views

urlpatterns = [

    path('formsubmit/', views.upload_file, name='input'),
    path('savecandles/', views.save_candle, name='savecandle'),
    path('convert_timeframe/',views.candle_timeframe,name='convertcandles'),
    path('download/',views.download_export,name='download_savejson.json')

]
