from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from public.forms import HospitalRegistrationForm, UserRegistrationForm
from public.models import Hospital, Personnel
import datetime, random, sha

def home(request):
    return render_to_response('index.html',{})

@csrf_exempt
def register(request):
	if request.POST:
		hospitalForm = HospitalRegistrationForm(request.POST)
		userForm = UserRegistrationForm(request.POST)
		
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
			
       	 	# Build activation_key and expiration time
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
			
			return HttpResponseRedirect('/login/')
	else:
		hospitalForm = HospitalRegistrationForm()
		userForm = UserRegistrationForm()

	return render_to_response('register.html',{'hospitalForm':hospitalForm, 'userForm':userForm,})# 'keyForm':keyForm})

@csrf_exempt
def login_user(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
		    if user.is_active:		        		        
				m = User.objects.get(username = username)
				u = Personnel.objects.get(user = m.id)
				request.session['mem_id'] = u.id
				request.session['hos_id'] = u.hospital
				
				login(request, user)
				return HttpResponseRedirect('/hospitalUser/') 
		    else:
		        state = "You have an inactive account, please contact the site admin."
		else:
		    state = "You entered either a wrong or non-existent username and/or password	."

	return render_to_response('login.html',{'state':state, 'username': username})
	
def logout_user(request):
    try:
		del request.session['mem_id']
		del request.session['hos_id']
		logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect('/')
