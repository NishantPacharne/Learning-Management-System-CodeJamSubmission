from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            usr_grp = request.user.groups.all()[0]
            if str(usr_grp) in allowed_roles:
                return view_func(request, *args, **kwargs)
            elif str(usr_grp) != request.user.groups.all()[0]:
                return redirect('dashboard_pg')
            else:
                return HttpResponse("You are not authorized")

        return wrapper_func
    return decorator

