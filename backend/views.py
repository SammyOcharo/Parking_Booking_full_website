from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect



# Create your views here.

from . models import PreBook, GetInTouch


def Home(request):


    return render(request, 'home.html')

def PreBooking(request):


    return render(request, 'prebooking.html')

def newBooking(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    location = request.POST.get("location")
    parking_slot = request.POST.get("parking_slot")
    parking_date = request.POST.get("parking_date")

    
    content=PreBook(Name=name, Email=email, Phone=phone, Location=location, Parking_Slot=parking_slot, Parking_Date=parking_date)
    content.save()


    return render(request, 'payment.html')

def Payment(request):
    
    
    return render(request, 'payment.html')

def About(request):


    return render(request, 'about.html')

def Contact(request):


    return render(request, 'contact.html')

def login(request):


    return render(request, 'login.html')

def Signup(request):


    return render(request, 'signup.html')

def newContact(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")

    content=GetInTouch(Name=name, Email=email, Message=message)
    content.save()


    return render(request, 'contact.html')


def Payment_successful(request):
    
    return render(request, 'success.html')


@csrf_exempt
def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['username'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("signup")
            except User.DoesNotExist:
                if len(username) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("signup")
                if not username.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("signup")
                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("signup")
        # create the user
        user = User.objects.create_user(username, email, password1)
        user.username = username
        user.save()
        messages.success(
            request, " Your account has been successfully created. Please navigate to Login to access your account")
        return redirect("home")
    else:
        return HttpResponse('404 - NOT FOUND ')
# view for rendering data from login page

def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        # cheching for valid login
         # cheching for valid login
        if user is not None:
            auth_login(request, user)
            print("user logged in")
            messages.success(request, " Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, " Invalid Credentials, Please try again....")
            return redirect("home")
    else:
        return render(request, 'signup')

@login_required
def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    print("we are logged out")
    return redirect('/')