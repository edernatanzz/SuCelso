from django.shortcuts import render


def profissional_home(request):
    return render(request,"profissional_template/home_template.html")