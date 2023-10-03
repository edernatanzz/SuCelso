from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.models import Courses, CustomUser, Students, Subjects


def profissional_home(request):
    return render(request,"profissional_template/home_template.html")
def visualizar_estudantes(request):
    # Recupere todos os estudantes do banco de dados
    students=Students.objects.all()
    return render(request, 'profissional_template/visualizar_estudantes.html', {"students":students})



def profissional_add_course(request):
    return render(request, "profissional_template/add_curso.html")

def profissional_add_course_save(request):
    if request.method == "POST":
        course = request.POST.get("course")
        if not course:
            messages.error(request, "O campo de nome do curso não pode estar em branco.")
            return HttpResponseRedirect("/profissional_add_course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Curso adicionado com sucesso")
            return HttpResponseRedirect("/profissional_add_course")
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao adicionar o curso: " + str(e))
            return HttpResponseRedirect("/profissional_add_course")
    else:
        return HttpResponse("Método não permitido")
    
    


def profissional_adicionar_conteudo(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    
    return render(request,"profissional_template/profissional_adicionar_conteudo.html",{"staffs":staffs,"courses":courses})
def profissional_adicionar_conteudo_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        staff_id = request.POST.get("staff")

        # Verificar se o campo subject_name está em branco
        if not subject_name:
            messages.error(request, "O campo de nome do conteúdo não pode estar em branco.")
            return HttpResponseRedirect("/profissional_adicionar_conteudo")

        try:
            course = Courses.objects.get(id=course_id)
            staff = CustomUser.objects.get(id=staff_id)

            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()

            messages.success(request, "Conteúdo adicionado com sucesso")
            return HttpResponseRedirect("/profissional_adicionar_conteudo")
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao adicionar conteúdo: " + str(e))
            return HttpResponseRedirect("/profissional_adicionar_conteudo")
        
        
        
        
def profissional_manage_course(request):
    courses=Courses.objects.all()
    return render(request, 'profissional_template/manage_course_template.html', {"courses":courses})


def profissional_editar_curso(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"profissional_template/manage_course_template.html",{"course":course,"id":course_id})

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def profissional_editar_curso_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Método não permitido</h2>")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course")

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect("/profissional_editar_curso_save"+course_id)
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao alterar dados: " + str(e))
            return HttpResponseRedirect("/profissional_editar_curso_save"+course_id)
        
        
        
