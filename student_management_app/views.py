from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from student_management_app.EmailBackEnd import EmailBackend


# ...

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin_home')
        else:
            messages.error(request,"Dados incorretos")
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