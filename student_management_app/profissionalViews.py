
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.models import Courses, Students


def profissional_home(request):
    return render(request,"profissional_template/home_template.html")
def visualizar_estudantes(request):
    # Recupere todos os estudantes do banco de dados
    students=Students.objects.all()
    return render(request, 'profissional_template/visualizar_estudantes.html', {"students":students})

