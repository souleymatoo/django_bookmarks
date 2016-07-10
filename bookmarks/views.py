from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
# Create your views here.

def main_page(request):
    output = '''
       <html>
         <head><title>%s</title></head>
         <body>
           <h1>%s</h1><p>%s</p>
         </body>
       </html>
     ''' % (
        'Django Bookmarks',
        'Welcome to Django Bookmarks',
        'Where you can store and share bookmarks!'
    )
    return HttpResponse(output)

def main_page1(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title': 'Django Bookmarks',
        'page_title': 'Welcome to Django Bookmarks',
        'page_body': 'Where you can store and share bookmarks!'
    })
    output = template.render(variables)
    return HttpResponse(output)