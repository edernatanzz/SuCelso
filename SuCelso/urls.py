from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from SuCelso import settings
from student_management_app import EstudanteViews, HodViews, profissionalViews, views

urlpatterns = [
    path('demo', views.showDemoPage, name="showDemoPage"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    path('', views.ShowLoginPage, name='ShowLoginPage'),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout_user"),
    path('doLogin', views.doLogin,name="doLogin"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    
    
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('add_course',HodViews.add_course,name="add_course"),
    path('add_course_save',HodViews.add_course_save,name="add_course_save"),
    path('add_student',HodViews.add_student,name="add_student"),
    path('add_student_save',HodViews.add_student_save,name="add_student_save"),
    path('add_subject',HodViews.add_subject,name="add_subject"),
    path('add_subject_save',HodViews.add_subject_save,name="add_subject_save"),
    
    
    path('manage_staff',HodViews.manage_staff,name="manage_staff"),
    path('manage_student',HodViews.manage_student,name="manage_student"),
    path('manage_course',HodViews.manage_course,name="manage_course"),
    path('manage_subject',HodViews.manage_subject,name="manage_subject"),
    
    
    path('editar_profissional/<str:staff_id>',HodViews.editar_profissional,name="editar_profissional"),
    path('editar_profissional_save',HodViews.editar_profissional_save,name="editar_profissional_save"),
    path('editar_estudante/<int:student_id>/',HodViews.editar_estudante, name="editar_estudante"),
    path('editar_estudante_save',HodViews.editar_estudante_save,name="editar_estudante_save"),
    path('editar_conteudo/<str:subject_id>', HodViews.editar_conteudo,name="editar_conteudo"),
    path('editar_conteudo_save', HodViews.editar_conteudo_save,name="editar_conteudo_save"),
    path('editar_curso/<str:course_id>', HodViews.editar_curso,name="editar_curso"),
    path('editar_curso_save', HodViews.editar_curso_save,name="editar_curso_save"),
    
    # Url para os profissionais
    path('profissional_home', profissionalViews.profissional_home,name="profissional_home"),
    path('estudante_home', EstudanteViews.estudante_home,name="estudante_home"),
    path('student_view_result',EstudanteViews.student_view_result,name="student_view_result"),

    
    
    
   
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
