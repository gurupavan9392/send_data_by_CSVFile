from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from project29.settings import CSV_DIR
from app.models import *
import csv

def insert_data(request):
    with open('C:\\Users\\Haritha\\OneDrive\\Desktop\\Django projects\\pavan\\Scripts\\project29\\Business-employment-data-september-2022-quarter-csv.csv','r') as file:
        OCF=csv.reader(file)
        header=next(OCF)
        for row in OCF:
             BO=BusinessEmpData(Series_reference=row[0],Period=row[1],Data_value=row[2],Suppressed=row[3],STATUS=row[4],UNITS=row[5],Magnitude=row[6],Subject=row[7],Group=row[8],Series_title_1=row[9],Series_title_2=row[10])
             BO.save()
    

    return HttpResponse('data inserted Successfully')




