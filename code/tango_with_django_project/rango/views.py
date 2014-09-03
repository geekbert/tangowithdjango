
from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response


# Create your views here.

from django.http import HttpResponse

def index(request):
   # return HttpResponse("Rango says hello world!<a href='/rango/about'>About</a>")
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
   # return HttpResponse("Rango says: Here is the about page!<a href='/rango/'>Index</a>")
    # Request the context of the request.
    # The context contains information such as the client's machine details,
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the templ
    context_dict = {'boldmessage': "I am a newly bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/about.html', context_dict, context)
