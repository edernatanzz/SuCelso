from django.shortcuts import render


def estudante_home(request):
    return render(request,"estudante_template/home_template.html")