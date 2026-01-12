from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def employee_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'employee_id' not in request.session:
            messages.error(request, "Please login to continue")
            return redirect('login')  # use your login URL name
        return view_func(request, *args, **kwargs)

    return _wrapped_view