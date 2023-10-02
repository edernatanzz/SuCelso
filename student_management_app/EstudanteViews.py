from django.shortcuts import render

from student_management_app.models import StudentResult, Students, Subjects


def estudante_home(request):
    return render(request,"estudante_template/home_template.html")

def student_view_result(request):
    student = Students.objects.get(admin=request.user.id)
    studentresult = StudentResult.objects.filter(student_id=student.id)
    
    # Recupere os assuntos (conteúdos) relacionados ao curso do aluno
    subjects_for_student = Subjects.objects.filter(course_id=student.course_id)
    
    return render(request, "estudante_template/conteudo_template.html", {
        "studentresult": studentresult,
        "subjects_for_student": subjects_for_student,  # Passe os assuntos do curso do aluno para o template
    })