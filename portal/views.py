from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from portal.forms import NewMessageForm, NewPatientForm, NewPersonnelForm
from portal.models import Message, Patient, MessageLog
from public.models import Personnel

@login_required(login_url='/login/')
def home(request):
    return render_to_response('hospitalUser/index.html',{})

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
    
    
@csrf_exempt
@login_required(login_url='/project/login/')
def viewMessages(request):
	messages = Message.objects.all()
	return render_to_response('hospitalUser/viewMessages.html',{'messages': messages})
	
    
@csrf_exempt
@login_required(login_url='/project/login/')
def viewPatients(request):
	patients = Patient.objects.all()
	return render_to_response('hospitalUser/viewPatients.html',{'patients': patients})

    
@csrf_exempt
@login_required(login_url='/project/login/')
def viewPersonnels(request):
	personnels = Personnel.objects.all()
	return render_to_response('hospitalUser/viewPersonnels.html',{'personnels': personnels})
	

@login_required(login_url='/project/login/')
def viewLog(request):
    messageLogList = MessageLog.objects.all()
    paginator = Paginator(messageLogList, 10) # Show 25 contacts per page

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

