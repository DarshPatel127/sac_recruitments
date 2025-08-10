from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# CSRF exempt decorator for class-based views
csrf_exempt_cbv = method_decorator(csrf_exempt, name='dispatch')
