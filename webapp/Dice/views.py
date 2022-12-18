import string
from django.urls import reverse
from django.shortcuts import render
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HTMLtextSerializers

from .models import*
import pandas as pd
import codecs
import json
import pickle

class main:
    def home(request):
        item = Character.objects.all().values()
        df = pd.DataFrame(item)
    
        mydict = {
            "df": df.to_html()
        }
        return render(request, 'index.html', context=mydict)

    def download(request):
        item = Character.objects.all().values()
        df = pd.DataFrame(item)   
        df.to_excel("output.xlsx")
        fileObj = open('output.xlsx','rb')
        response = HttpResponse(fileObj, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="dicecharacter.xlsx"'
        return(response)


class dice_view(APIView):   
    def get(self, request):
        k = {}
        excel_data = pd.read_excel('output.xlsx')
        df = pd.DataFrame(excel_data)
        # z = request.get_host() + '/download'
        z ='http://' + request.get_host() + '/download'
        a = df.to_dict()
        k['zadacha'] = a
        k['url'] = z 
        return Response(k)

