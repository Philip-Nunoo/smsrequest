from django.shortcuts import render_to_response

from patientProject.forms import HospitalRegistrationForm, RegistrationForm, LoginForm, NewMessageForm, KeyForm
from patientProject.models import Hospital, Personnel
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime, random, sha

def index(request):
    return render_to_response('index.html',{})

@csrf_exempt
def registerUser(request):
    if request.POST:
        hospitalForm = HospitalRegistrationForm(request.POST)
        userForm = RegistrationForm(request.POST)
        
        if hospitalForm.is_valid() and userForm.is_valid():
            # Fields from hospital form
            hospital_name = hospitalForm.cleaned_data['hospital_name']
            postal_address = hospitalForm.cleaned_data['postal_address']
            location = hospitalForm.cleaned_data['location']
            email = hospitalForm.cleaned_data['email']
            contact_number = hospitalForm.cleaned_data['contact_number']
            
            # Fields from user Form
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
            personnel_type = userForm.cleaned_data['personnel_type']
            user_email = userForm.cleaned_data['email']
            
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            
            #### other fields for the personnnel
            # Build activation_key
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+username).hexdigest()
            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            #create User object
            user = User.objects.create_user(username, user_email, password)
            
            #create hospital object
            hospital = Hospital.objects.create(
                            hospital_name = hospital_name, 
                            postal_address = postal_address,
                            location = location,
                            email = email,
                            contact_number = contact_number
                        )
            
            # Now we can create Personnel object passing hospital and user objects
            personnel = Personnel.objects.create(
                            first_name = first_name,
                            last_name = last_name,
                            personnel_type = personnel_type,
                            email = user_email,
                            activation_key = activation_key,
                            key_expires = key_expires,
                            hospital = hospital,
                            user = user
                        )
            
            # user.is_active = False;
            ## Save the User object
            user.save()
            ## Save the Hospital object
            hospital.save()
            ## Save the personnel object
            personnel.save()
            print "hospitalForm is valid"
            return HttpResponseRedirect('/project/loginUser')
    else:
        hospitalForm = HospitalRegistrationForm()
        userForm = RegistrationForm()
        keyForm = KeyForm()
    #userForm = forms.FormWrapper(userForm, new_data, errors)
    return render_to_response('register.html',{'hospitalForm':hospitalForm, 'userForm':userForm,})# 'keyForm':keyForm})

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                m = User.objects.get(username = username)
                u = Personnel.objects.get(user = m.id)
                request.session['mem_id'] = u.id
                request.session['hos_id'] = u.hospital
                login(request, user)
                return HttpResponseRedirect('/hospitalUser/')       
            
        return HttpResponseRedirect('/project/')
    else:
        form = LoginForm()
    return render_to_response('login.html',{'loginForm': form})

def logoutUser(request):
    logout(request)
    #del request.session['mem_id']
    #del request.session['hos_id']
    return HttpResponseRedirect('/project/')