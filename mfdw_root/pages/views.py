from django.shortcuts import render
# from django.http import HttpResponse
from . models import Page

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'contect':pg.bodytext,
        'last_update': pg.update_date,
    }
    # assert False
    return render(request, 'pages/page.html', context)