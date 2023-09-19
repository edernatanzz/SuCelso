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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
