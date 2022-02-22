from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='home'),
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    path('pre-booking', views.PreBooking, name='prebooking'),
    path('new-booking/', views.newBooking, name='newbooking'),
    path('new-contact/', views.newContact, name='newcontact'),
    path('payment/', views.Payment, name='payment'),
    path('payment-successful/', views.Payment_successful, name='payment-successful'),
    path('handlesignup/', views.handlesignup, name="handlesignup") ,
    path('handlelogin/', views.handlelogin, name="handlelogin") ,
    path('signup/', views.Signup, name="signup") ,
    path('login/', views.login, name="login") ,
     path('handlelogout/', views.handlelogout, name="handlelogout"),
]