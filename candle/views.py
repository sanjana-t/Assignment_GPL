from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .forms import UploadFileForm
from .models import Candle,UploadFile
import re
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from django.db.models import Min
import json
from django.http import HttpResponse
from django.http import FileResponse
# Create your views here.
# views.py

# Input from user through forms.py is stored in the model UploadFile and 
# File is stored on server 
# timeframe for calculation is picked from last record on model

@api_view(['POST'])
def upload_file(request):
    if request.method =='POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            newform = UploadFile(csv_file=request.FILES['csv_file'])
            newform.save()
    return HttpResponseRedirect('/success/url')

#save data to db
#picking the data from the server
#storing the data as each object on to the model Candle
#with attributes as id,name,date,time,open,high,low,close,volume 
@api_view(['GET'])
def save_candle(request):
    with open(r'candle\NIFTY_F1_Xm8mAtb.txt') as ifile:
        for line in ifile:
        # s=ifile.readline()
            m = re.split(',',line)
            print(m)
            print(line)
            Candle.objects.get_or_create(
                name = m[0],
                date = m[1],
                time = m[2],
                open = m[3],
                high = m[4],
                low = m[5],
                close = m[6],
                volume = m[7])
    return Response({"success":"success"},status=status.HTTP_200_OK)

# converting the candles into a given timeframe
# storing the data into json file by generating the file
@api_view(['GET'])
def candle_timeframe(request):
    data={}
    data["list"]=[]
    count_candle = Candle.objects.count()
    print(count_candle)
    time=UploadFile.objects.all().last()
    print(time.timeframe)
    for i in range(0, count_candle, time.timeframe):
        candle = Candle.objects.filter()[i:i+10]
        open_query = Candle.objects.filter()[i]
        close_query = Candle.objects.filter()[i+9]
        max_value=candle.aggregate(Max('high'))
        min_value=candle.aggregate(Min('low'))
        timeframecandle =[open_query.name,open_query.date,open_query.time,open_query.open,max_value["high__max"],min_value["low__min"],close_query.close,close_query.volume]
        data['list'].append(timeframecandle)
        save_file = open("savedata.json", "w")  
        json.dump(data, save_file, indent = 6,default=str)  
        save_file.close()  
    return Response({"success":"success","data":data},status=status.HTTP_200_OK)


#download the stored file
#on triggering the api a download.json file gets downloaded on system
#this download api can be used to triggered through a button on frontend
@api_view(['GET'])
def download_export(request):
    response = FileResponse(open("savedata.json", 'rb'), as_attachment=True,
                            filename="download.json")
    return response

            
                    