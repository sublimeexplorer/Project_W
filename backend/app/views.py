from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm
from .forms import MemberCreationForm
from .models import Member


# from . import helpers as _

################################
# TODO:
# - DJANGO MIGRATIONS (X)
# - CONNECT SERVER (VIEWS) TO DATABASE (X)
# - CHECK_INPUT_VALIDITY
# - ADD USER TO DATABASE (X)
# - LOGIN PAGE (X)
# - AUTHENTICATE LOGIN PROCESS
# - ONLY SHOW "HOME" PAGE IF LOGIN IS VALIDATED/AUTHENTICATED
# - SESSION
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
        


@csrf_protect
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                # messages.success(request, 'Login successful!')
                print('Login successful')
                return redirect('home')  # Redirect to home page or dashboard
            else:
                # messages.error(request, 'Invalid email or password')
                print('Invalid email or password')
        else:
            # messages.error(request, 'Invalid form submission')
            print('Invalid form submission')
    else:
        form = LoginForm()
    
    return render(request, 'app/login.html', {'form': form})

def logout(request):
    return HttpResponse("logout page")
    # return render(request, 'app/login.html')

def get_user(request):
    pass

