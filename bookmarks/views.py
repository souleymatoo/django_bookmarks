from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

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
        'page_body': 'Where you can store and share bookmarks!',
        'user': request.user
    })
    output = template.render(variables)
    return HttpResponse(output)

def main_page2(request):

        return render_to_response(
                'main_page.html',
                {
                    'user': request.user,
                    'fullname' : request.user.get_full_name() if request.user.username else ''
                  }
        )

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')
    bookmarks = user.bookmark_set.all()
    template = get_template('user_page.html')

    variables = Context({
        'username': username,
        'firstname': user.first_name,
        'lastname': user.last_name,
        'bookmarks': bookmarks
    })
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):

    request.session.flush()

    logout(request)

    return HttpResponseRedirect('/login')