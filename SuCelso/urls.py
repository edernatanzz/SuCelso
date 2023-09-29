from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from SuCelso import settings
from student_management_app import HodViews, views

urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('doLogin', views.doLogin),
    path('admin_home',HodViews.admin_home),
    path('add_staff',HodViews.add_staff),
    path('add_staff_save',HodViews.add_staff_save),
    path('add_course',HodViews.add_course),
    path('add_course_save',HodViews.add_course_save),
    path('add_student',HodViews.add_student),
    path('add_student_save',HodViews.add_student_save),
    path('add_subject',HodViews.add_subject),
    path('add_subject_save',HodViews.add_subject_save),
    path('manage_staff',HodViews.manage_staff),
    path('manage_student',HodViews.manage_student),
    path('manage_course',HodViews.manage_course),
    path('manage_subject',HodViews.manage_subject),
    path('editar_profissional/<str:staff_id>',HodViews.editar_profissional),
    path('editar_profissional_save',HodViews.editar_profissional_save),
    path('editar_estudante/<int:student_id>/',HodViews.editar_estudante),
    path('editar_estudante_save',HodViews.editar_estudante_save),
    
    path('editar_conteudo/<str:subject_id>', HodViews.editar_conteudo,name="editar_conteudo"),
    path('editar_conteudo_save', HodViews.editar_conteudo_save,name="editar_conteudo_save"),
    path('editar_curso/<str:course_id>', HodViews.editar_curso,name="editar_curso"),
    path('editar_curso_save', HodViews.editar_curso_save,name="editar_curso_save"),

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
