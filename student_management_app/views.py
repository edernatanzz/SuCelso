import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_management_app.EmailBackEnd import EmailBackend


# ...
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Use o EmailBackend personalizado para autenticação
        email_backend = EmailBackend()
        user = email_backend.authenticate(request, username=email, password=password)

        if user is not None:
            # Autenticação bem-sucedida
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("profissional_home"))
            else:
                return HttpResponseRedirect(reverse("estudante_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")
    
#modelo 
#def name(request):
   # return render(request,".html")
# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+ request.user.email+"usertype : "+ request.user.user_type)
    else:
        return HttpResponse("Por favor faça login primeiro ")
 
def logout_user(request):
    logout(request) 
    return HttpResponseRedirect("/")