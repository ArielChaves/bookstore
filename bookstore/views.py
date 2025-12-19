"""
Views for bookstore project root.
"""
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git


def home(request):
    """
    Root endpoint that provides information about available API endpoints.
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bookstore API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
            }
            h2 {
                color: #555;
                margin-top: 30px;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                padding: 10px;
                margin: 5px 0;
                background: #f8f9fa;
                border-left: 4px solid #007bff;
            }
            a {
                color: #007bff;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
            .endpoint {
                font-family: monospace;
                color: #28a745;
            }
            .version {
                color: #6c757d;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 Bookstore API</h1>
            <p class="version">Version 1.0</p>
            
            <h2>Available Endpoints</h2>
            <ul>
                <li>
                    <strong>Admin Panel:</strong> 
                    <a href="/admin/" class="endpoint">/admin/</a>
                </li>
                <li>
                    <strong>API Token Auth:</strong> 
                    <a href="/api-token-auth/" class="endpoint">/api-token-auth/</a>
                </li>
                <li>
                    <strong>API v1 Base:</strong> 
                    <a href="/bookstore/v1/" class="endpoint">/bookstore/v1/</a>
                </li>
                <li>
                    <strong>API v2 Base:</strong> 
                    <a href="/bookstore/v2/" class="endpoint">/bookstore/v2/</a>
                </li>
            </ul>
            
            <h2>API Documentation</h2>
            <ul>
                <li>
                    <strong>Products:</strong> 
                    <a href="/bookstore/v1/product/" class="endpoint">/bookstore/v1/product/</a>
                </li>
                <li>
                    <strong>Categories:</strong> 
                    <a href="/bookstore/v1/category/" class="endpoint">/bookstore/v1/category/</a>
                </li>
                <li>
                    <strong>Orders:</strong> 
                    <a href="/bookstore/v1/order/" class="endpoint">/bookstore/v1/order/</a>
                </li>
            </ul>
            
            <p style="margin-top: 30px; color: #6c757d; font-size: 0.9em;">
                Django REST Framework browsable API is available at each endpoint.
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)


@csrf_exempt
def update(request):
    """
    Webhook endpoint to receive GitHub notifications and update code automatically.
    """
    if request.method == "POST":
        '''
        pass the path of the directory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "bookstore"
        '''
        repo = git.Repo('/home/arielchaves/bookstore')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


def hello_world(request):
    """
    Simple hello world view that renders a template.
    """
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())

