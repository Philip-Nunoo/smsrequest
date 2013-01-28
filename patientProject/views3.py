# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from patientProject.sendmessage import sendMessage
from django.contrib.auth import authenticate, login
import datetime, random, sha
from django.core.mail import send_mail

from patientProject.models import Personnel
from patientProject.forms import NewPatientForm, NewHospitalForm, NewMessageForm, LoginForm, RegistrationForm


def index(request):
    return render_to_response('index.html',{})

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print "login success"
                # Redirect to a success page.
            else:
                print "Disabled account"
                # Return a 'disabled account' error message
        else:
            print "Invalid login"
            # Return an 'invalid login' error message.
            
        return HttpResponseRedirect('/project/')
    else:
        form = LoginForm()
    return render_to_response('login.html',{'loginForm': form})

def registerUser(request):
    '''
    This registers both the initial hospital plus
    the initial admin account
    
    1. Check if it's a post request
    2. Validate all entries 
        i. Validate the fields for the hospital form
        ii. Validate the fields for the user form
    3. Get the hospital_id and insert it into the user hospital field
    4. 
    '''
    if request.user.is_authenticated():
        # User already have an account: no registration
        return render_to_response('/project/register', {'has_account': True})
    
    manipulator = RegistrationForm()
    if request.POST:
        new_data = request.POST.copy()
        errors = manipulator.get_validation_errors(new_data)
        
        if not errors:
            # save the user
            manipulator.do_html2python(new_data)
            new_user = manipulator.save(new_data)
            
            # Building the activation key for the account
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+new_user.username).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            # Creating user
            new_personnel = Personnel(
                                first_name = "",
                                last_name = "",
                                hospital = "",
                                personnel_type = "",
                                activation_key = "",
                                key_expires ="",
                            )
            new_personnel.save()
            
            
            # send email to user
            email_subject = 'Your new localhost:8000 account confirmation code'
            email_body = "Hello, %s, and thanks for signing up for an account from our service!\n\nTo activate your account, click this link within 48 hours:\n\nhttp://localhost:8000/accounts/confirm/%s" % (new_user.username, new_personnel.activation_key)
            send_mail(email_subject, email_body, 'accounts@example.com', [new_user.email])
            
            return render_to_response('register.html', {'created': True})
        else:
            errors = new_data = {}
        form = forms.FormWrapper(manipulator, new_data, errors)
    return render_to_response('register.html',{'hospitalForm': hospitalForm, 'userForm':userForm})

@csrf_exempt
def newPatient(request):    
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/project/')
    else:
        form = NewPatientForm()
        
    return render_to_response('addNewPatient.html',{'newPatientForm': form})

@csrf_exempt
def newHospital(request):
    if request.method == 'POST':
        form = NewHospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/project/")
    else:
        form = NewHospitalForm()
            
    return render_to_response('addNewHospital.html',{'newHospitalForm': form})

@csrf_exempt
def createNewMessage(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            message_frequency = request.POST['message_frequency']
            message_form = form.save(commit = False)
            
            if (message_frequency == "once"):
                message_form.active = False
                sendMessage()
                request.POST['active']
            elif (message_frequency == "specify"):
                message_form.active = True
            else:
                #Message would start sending the following day and frequency would be added there of
                message_form.active = True
                message_form.start_at_date = message_form.start_at_date + datetime.timedelta(days=1)
                       
            message_form.save()
            return HttpResponseRedirect("/project/")
    else:
        form = NewMessageForm()
    
    return render_to_response('createNewMessage.html',{'newMessageForm': form})