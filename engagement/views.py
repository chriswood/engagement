
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from engagement.graphing.utilities import build_chart

def engagement(request):
    kwargs = {
        'chf' : 'c,lg,0,EFEFEF,0,BBBBBB,1', #chart_colors
        'chxt' : 'x,y', #visible_axis
        'chxl' : '1:|User1|User2|User3|User4|User5', #y axis
        'chbh' : 'a', #bar_width
        'chs' : '800x360', #chart_size
        'cht' : 'bhs', #chart_type
        'chco' : '80C65A,0F9E00,2C58C6,FF3030', #colors
        'chd' : 'e:MzHCHCMzGZ,DMJmHCGZTM,GZMzDMGZFH,FHHrPWI9Fw', #data
        'chdl' : 'opens|clicks|forwards|shares', #labels
        'chtt' : "Im in ur response analysing your d00ds", #title
        'chts' : '676767,19.5', #style
    }

    context = {
        'chart_url' : build_chart(**kwargs),
    }
    
    return render_to_response('main.html', context,
               context_instance=RequestContext(request))
               