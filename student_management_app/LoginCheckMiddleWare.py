from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "student_management_app.profissionalViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("profissional_home"))
            elif user.user_type == "3":
                if modulename == "student_management_app.EstudanteViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("estudante_home"))
            else:
                return HttpResponseRedirect(reverse("ShowLoginPage"))

        else:
            if request.path == reverse("ShowLoginPage") or request.path == reverse("doLogin"):
                pass
            else:
                return HttpResponseRedirect(reverse("ShowLoginPage"))