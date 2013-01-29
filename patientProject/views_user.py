from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from patientProject.forms import NewMessageForm, NewPatientForm, NewPersonnelForm
from patientProject.sendmessage import sendMessageNow
from patientProject.models import MessageLog

import datetime

@login_required(login_url='/project/login/')
def index(request):
    return render_to_response('hospitalUser/index.html',{})
    #return HttpResponse ("You are logged in")

@csrf_exempt
@login_required(login_url='/project/login/')
def createNewMessage(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            message_frequency = request.POST['message_frequency']
            message_form = form.save(commit = False)
            
            print message_form.id;
            
            if (message_frequency == "once"):
                # Bug loggin
                message_form.active = False
                receipient_id = request.POST['receipient_name']
                message = request.POST['message_content']                
                sendMessageNow(message, receipient_id)
            else:
            
                message_form.active = True  # making the message active should change later
            
            message_form.save()            
            return HttpResponseRedirect("/hospitalUser/")
    else:
        form = NewMessageForm()
    
    return render_to_response('hospitalUser/createNewMessage.html',{'newMessageForm': form})

@csrf_exempt
@login_required(login_url='/project/login/')
def addNewPatient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():         
            form.save()
            return HttpResponseRedirect("/hospitalUser/")
    else:
        form = NewPatientForm()
    
    return render_to_response('hospitalUser/addNewPatient.html',{'newPatientForm': form})

@csrf_exempt
@login_required(login_url='/project/login/')
def addPersonnel(request):
    if request.POST:
        form = NewPersonnelForm(request.POST)
        if form.is_valid():
            #form.save()
            return HttpResponseRedirect("/hospitalUser/")
    else:
        form = NewPersonnelForm()
    
    return render_to_response('hospitalUser/addPersonnel.html',{'newPersonnelForm': form})

def viewLog(request):
    messageLogList = MessageLog.objects.all()
    paginator = Paginator(messageLogList, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        log = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        log = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        log = paginator.page(paginator.num_pages)
        
    return render_to_response('hospitalUser/log.html',{'messageLog': log})