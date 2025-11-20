# api/decorators.py
from functools import wraps
from django.http import JsonResponse

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse({'success': False, 'message': 'Authentication required'}, status=401)
            if request.user.role != role:
                return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=403)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
