
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def engagement(request):
    context = {}
    return render_to_response('main.html', context,
               context_instance=RequestContext(request))
    

