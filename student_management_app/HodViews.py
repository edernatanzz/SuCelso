from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from student_management_app.models import Courses, CustomUser, Students
from django.contrib import messages


def admin_home(request):
    return render(request, 'hod_template/home_content.html')

def add_staff(request):
    return render(request, 'hod_template/add_staff_template.html')

def add_staff_save(request):
    if request.method!= 'POST':
        return HttpResponse('Method not allowed')
    else:
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        try:
            user=CustomUser.objects.create_user(username=username, password=password,  email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request="Profisional Adicionado com sucesso")
            return HttpResponseRedirect("/add_staff")
            
        except:
            messages.error(request="Ops , algo deu errado ao adicionar profissional")
            return HttpResponseRedirect("/add_staff")
        from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from student_management_app.models import CustomUser
from django.contrib import messages

def admin_home(request):
    return render(request, 'hod_template/home_content.html')

def add_staff(request):
    return render(request, 'hod_template/add_staff_template.html')

def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            
            messages.success(request, "Profissional adicionado com sucesso")
            return HttpResponseRedirect("/add_staff")
            
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao adicionar o profissional: " + str(e))
            return HttpResponseRedirect("/add_staff")

def add_course(request):
    return render(request, "hod_template/add_course_template.html")

def add_course_save(request):
    if request.method == "POST":
        course = request.POST.get("course")
        if not course:
            messages.error(request, "O campo de nome do curso não pode estar em branco.")
            return HttpResponseRedirect("/add_course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Curso adicionado com sucesso")
            return HttpResponseRedirect("/add_course")
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao adicionar o curso: " + str(e))
            return HttpResponseRedirect("/add_course")
    else:
        return HttpResponse("Método não permitido")
    
def add_student(request):
    courses = Courses.objects.all()
    return render(request, "hod_template/add_student_template.html",{'courses': courses})

def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Método não permitido')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_id = request.POST.get('course')
        sex = request.POST.get('sex')

        try:
            course_id = int(course_id)
            course_obj = Courses.objects.get(id=course_id)
        except (ValueError, Courses.DoesNotExist):
            messages.error(request, "Curso inválido selecionado.")
            return HttpResponseRedirect("/add_student")

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.students.address = address
            user.students.course = course_obj
            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.students.profile_pic = ""
            user.students.gender = sex
            user.save()

            messages.success(request, "Estudante adicionado com sucesso!")
            return HttpResponseRedirect("/add_student")

        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao adicionar o estudante: " + str(e))
            return HttpResponseRedirect("/add_student")

    # Certifique-se de retornar um HttpResponse em todos os casos
    return HttpResponse('Algo deu errado ao processar a solicitação.')