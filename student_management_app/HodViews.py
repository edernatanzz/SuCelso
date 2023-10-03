from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from student_management_app.models import Courses, CustomUser, Staffs, Students, Subjects
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

def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    
    return render(request,"hod_template/add_subject_template.html",{"staffs":staffs,"courses":courses})
def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        staff_id = request.POST.get("staff")

        # Verificar se o campo subject_name está em branco
        if not subject_name:
            messages.error(request, "O campo de nome do conteúdo não pode estar em branco.")
            return HttpResponseRedirect("/add_subject")

        try:
            course = Courses.objects.get(id=course_id)
            staff = CustomUser.objects.get(id=staff_id)

            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()

            messages.success(request, "Conteúdo adicionado com sucesso")
            return HttpResponseRedirect("/add_subject")
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao adicionar conteúdo: " + str(e))
            return HttpResponseRedirect("/add_subject")
        
def manage_staff(request):
    staffs = Staffs.objects.all()  # Supondo que você tenha um modelo chamado Staffs para armazenar informações sobre os funcionários.
    return render(request, 'hod_template/manage_staff_template.html',{"staffs":staffs})

def manage_student(request):
    students=Students.objects.all()
    return render(request, 'hod_template/manage_student_template.html', {"students":students})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request, 'hod_template/manage_course_template.html', {"courses":courses})
def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request, 'hod_template/manage_subject_template.html', {"subjects":subjects})

def editar_profissional(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id )
    return render(request, 'hod_template/editar_profissional_template.html', {"staff":staff,"id":staff_id})    

def editar_profissional_save(request):
    if request.method!="POST":
        return HttpResponse("<h2> Metodo não permitido </h2>")
    else:
        staff_id=request.POST.get('staff_id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        address=request.POST.get('address')
        
        try:        
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.address=address
            user.save()
            
            
            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect("/editar_profissional/"+staff_id)
        
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao alterar dados : " + str(e))
            return HttpResponseRedirect("/editar_profissional/"+staff_id)
            
            
            
def editar_estudante(request, student_id):
    student=Students.objects.get(admin=student_id)
    courses=Courses.objects.all()
    return render(request,"hod_template/editar_estudante_template.html", {"student":student,"courses": courses,"id":student_id})
    

def editar_estudante_save(request):
    if request.method!='POST':
        return HttpResponse("Metodo não permitido ")
    else:
        student_id=request.POST.get("student_id")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_id = request.POST.get('course')
        sex = request.POST.get('sex')
        
        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()
            
            student=Students.objects.get(admin=student_id)
            student.address=address
            student.session_start_year=session_start
            student.session_end_year=session_end
            student.gender=sex
            
            course=Courses.objects.get(id=course_id)
            student.course_id=course
            student.save()
            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect("/editar_estudante/"+student_id)
        
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao alterar dados : " + str(e))
            return HttpResponseRedirect("/editar_estudante/"+student_id)
                
            
            
def editar_conteudo(request, subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/editar_conteudo_template.html",{"subject":subject,"staffs":staffs,"courses":courses,"id":subject_id})

def editar_conteudo_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect("/editar_conteudo/"+subject_id)
        
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao alterar dados : " + str(e))
            return HttpResponseRedirect("/editar_conteudo/"+subject_id)

def editar_curso(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/editar_curso.html",{"course":course,"id":course_id})

def editar_curso_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Método não permitido</h2>")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course")
        course_image = request.FILES.get("course_image")

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            if course_image:
                course.course_image = course_image
            course.save()
            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect("/editar_curso/"+course_id)
        except Exception as e:
            messages.error(request, "Ops, algo deu errado ao alterar dados: " + str(e))
            return HttpResponseRedirect("/editar_curso/"+course_id)

        
        
def course_subjects(request, course_id):
    # Recupere o curso com base no course_id
    course = Courses.objects.get(id=course_id)

    # Recupere os assuntos (conteúdos) associados a esse curso
    subjects = Subjects.objects.filter(course_id=course)
    return render(request, 'hod_template/conteudo_template.html', {'course': course, 'subjects': subjects})
