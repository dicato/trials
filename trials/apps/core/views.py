# stardard library imports

# django imports
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response


def index(request):
    """
    The homepage.
    """
    return render_to_response('index.html')


def about(request):
    """
    The about page.
    """
    return render_to_response('about.html')


def contact(request):
    """
    The contact page.
    """
    return render_to_response('contact.html')
