
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from engagement.graphing.utilities import build_chart

def engagement(request):
    kwargs = {
        'base' : 'http://chart.apis.google.com/chart?',
        'chart_colors' : 'chf=c,lg,0,EFEFEF,0,BBBBBB,1',
        'y-axis' : '&chxl=1:|User1|User2|User3|User4|User5'
        
    }

    context = {
        'chart_url' : build_chart(**kwargs),
    }
    return render_to_response('main.html', context,
               context_instance=RequestContext(request))
    

