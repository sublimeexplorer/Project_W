from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from .forms import MemberCreationForm
from .models import Member
from django.contrib import messages
from django.contrib.auth import get_user_model


# from . import helpers as _

################################
# TODO:
# - DJANGO MIGRATIONS (X)
# - CONNECT SERVER (VIEWS) TO DATABASE
# - CHECK_INPUT_VALIDITY
# - ADD USER TO DATABASE
# - LOGIN PAGE (X)
# - AUTHENTICATE LOGIN PROCESS
# - ONLY SHOW "HOME" PAGE IF LOGIN IS VALIDATED/AUTHENTICATED
# - SESSION (?)
################################


def home(request):
    current_user = None
    return render(request, 'app/home.html')

def get_all_members(request):
    User = get_user_model()
    users = User.objects.all()
    print(users)
    return render(request, 'app/members_list.html', {'users': users})

def register(request):    
    if request.method == 'POST':
        print('request is POST')
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('user added to database')
            
            return HttpResponse("user added to database")
            # login(request, user)
            # return redirect('home')  # Redirect to home page after successful registration
        else:
            print('Form is not valid')
            print('Form errors:', form.errors)
    else:
        print('not POST')
        form = MemberCreationForm()
    return render(request, 'app/register.html', {'form': form}) 
        


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Try to find a member with the provided email
            member = Member.objects.get(email=email)
            
            # Check if the password matches
            if member.password == password:  # Note: This is not secure, see below
                # Successful login
                # messages.success(request, 'Login successful!')
                print('login successful')
                # You might want to set up a session here
                return redirect('home')  # Redirect to home page or dashboard
            else:
                # messages.error(request, 'Invalid password')
                print('Invalid entry')
        except Member.DoesNotExist:
            # messages.error(request, 'No account found with this email')
            print('No account found with this email')
    
    return render(request, 'app/login.html')

def get_user(request):
    pass

