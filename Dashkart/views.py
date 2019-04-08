from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import LoginForm, SignupForm, AddpatForm, SearchpatForm
from .models import *
from django.db import connection
from collections import Counter
from django.utils import timezone
from django.forms.models import model_to_dict
import datetime
import random
import numpy as np
import json
import serial
import os
import math

def login(request):
	if request.method == 'POST':
		request.session.flush()
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.get(email = email)
			if user.password == password :
				print("Go to home")
				request.session['first_name'] = user.first_name
				request.session['id'] = user.id
				request.session['wallet'] = user.wallet
				return render(request,'Dashkart/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'],  'mssg':'','wallet':request.session['wallet']})	
			else:
				return render(request,'Dashkart/',{})
	else:		
		return render(request,'Dashkart/index.html',{})

def signup(request):
	if request.method == 'POST':
		request.session.flush()
		form = SignupForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			obj = User.objects.create() 
			obj.first_name = first_name
			obj.last_name = last_name
			obj.email = email
			obj.password = password
			obj.wallet = "1000"
			obj.save()
			request.session['first_name'] = first_name
			request.session['id'] = obj.id
			request.session['wallet'] = obj.wallet

			return render(request,'Dashkart/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'], 'mssg' : '', 'wallet':request.session['wallet'] })	
	else:		
		return render(request,'Dashkart/signup.html',{})

def home(request):
	return render(request,'Dashkart/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'],'count': count,'mssg':'','wallet':request.session['wallet']})	

def addpat(request):
	if request.method == 'POST':
		form = AddpatForm(request.POST)
		if form.is_valid():
			obj = Patient.objects.create(age=form.cleaned_data['age']) 
			obj.first_name = form.cleaned_data['first_name']
			obj.last_name = form.cleaned_data['last_name']
			obj.email = form.cleaned_data['email']
			obj.address = form.cleaned_data['address']
			obj.gender = form.cleaned_data['gender']
			obj.age = form.cleaned_data['age']
			obj.contact_no = form.cleaned_data['contact_no']
			obj.doc = Doctor.objects.get(id=request.session.get('id'))
			obj.save()
			mssg="Patient added successfuly"
			count = Patient.objects.all().count()
			return render(request,'Dashkart/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'], 'count' : count,'mssg' : mssg })
		else:
			print("dsfsdfsd")
def searchpat(request):
	if request.method == 'POST':
		form = SearchpatForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			mobile = form.cleaned_data['mobile']
			if first_name:
				pat_obj = Patient.objects.get(first_name = first_name) 
			else:
				pat_obj = Patient.objects.get(contact_no = mobile) 
			if pat_obj:
				request.session['pat'] = pat_obj.id
				first_name = pat_obj.first_name
				last_name = pat_obj.last_name
				age = pat_obj.age
				gender = pat_obj.gender
				address = pat_obj.address
				contact_no = pat_obj.contact_no
				#return render(request,'Dashkart/patient.html',{'first_name':first_name, 'last_name': last_name, 'age': age,'gender': gender,'address': address,'contact_no': contact_no})				
				return render(request,'Dashkart/patient.html',{'pat':pat_obj})				
			else:
				print("Patient not found!")
				return render(request,'Dashkart/home.html',{})
							
def patient(request):
	pat_obj = Patient.objects.get(id=request.session['pat']) 
	return render(request,'Dashkart/patient.html',{'pat':pat_obj})

def vitaltest(request):
	pat_obj = Patient.objects.get(id=request.session['pat']) 
	return render(request,'Dashkart/vitaltest.html',{'pat':pat_obj})

def test(request):
	pat_obj = Patient.objects.get(id=request.session['pat'])
	try:
		lhr =(list(PressureReading.objects.filter(pat_id = request.session['pat'] , hand="left", type_of_reading = "F23").values('id','pat_id_id','mean_pressure','hand','type_of_reading','time')))
	except PressureReading.DoesNotExist:
		lhr = []
	try:
		rhr = list(PressureReading.objects.filter(pat_id = request.session['pat'] , hand="right" , type_of_reading = "F23" ).values()) 
	except PressureReading.DoesNotExist:
		rhr = []
	return render(request,'Dashkart/test.html',{'pat' : pat_obj, 'lhr':lhr, 'rhr':rhr,'first_name': request.session['first_name'], 'id' : request.session['id']})

def changeReading(request):
	data = dict()
	tor = request.GET.get('slct',None)
	try:
		lhr = list(PressureReading.objects.filter(pat_id = request.session['pat'] , hand="left", type_of_reading = tor).values())	
	except PressureReading.DoesNotExist:
		lhr = []
	try:
		rhr = list(PressureReading.objects.filter(pat_id = request.session['pat'] , hand="right" , type_of_reading = tor ).values()) 
	except PressureReading.DoesNotExist:
		rhr = []
	data['lhr'] = lhr
	data['rhr'] = rhr
	return JsonResponse(data)

def getPressure(request):
    # ser = serial.Serial('/dev/ttyUSB0',9600)
    # s = [0]
    # read_serial=ser.readline()
    # s[0] = int (ser.readline(),16)
    # s[0] = math.ceil(((s[0]-55)*100)/11.85)/100
	data = dict()
	#data['pressure'] = s[0]
	data['pressure'] = random.randint(1,1024)
	return JsonResponse(data)

def storePressure(request):
	data = dict()
	pat_id = request.GET.get('id',None)
	p = PressureReading.objects.create(pat_id = Patient.objects.get(id = pat_id), mean_pressure = request.GET.get('mean',None), hand = request.GET.get('side',None), type_of_reading =request.GET.get('type',None), time=request.GET.get('time',None) )
	p.save()
	print(p)
	return JsonResponse(data)


