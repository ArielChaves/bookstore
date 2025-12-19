"""
Views for bookstore project root.
"""
from django.http import JsonResponse


def home(request):
    """
    Root endpoint that provides information about available API endpoints.
    """
    return JsonResponse({
        'message': 'Bookstore API',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'api_token_auth': '/api-token-auth/',
            'bookstore_v1': '/bookstore/v1/',
            'bookstore_v2': '/bookstore/v2/',
            'api_documentation': {
                'products': '/bookstore/v1/product/',
                'categories': '/bookstore/v1/category/',
                'orders': '/bookstore/v1/order/',
            }
        }
    })

