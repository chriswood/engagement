from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from engagement.graphing.utilities import (
    build_chart,
    get_users,
    format_data,
    default_chart,
    get_user_data,
)
from engagement.forms import EngagementForm
from criteria_build import CriteriaBuild

def engagement(request):
    users_count = 0
    if request.method == 'POST':
        form = EngagementForm(request.POST)
        if form.is_valid():
            criteria = {}
            crit_list = []
            users_count = form.cleaned_data['number_of_users']
            
            #put together criteria from form
            for element in form.cleaned_data:
                if element[-6:] == 'weight':
                    criteria[element[:-7]] = form.cleaned_data[element]
                    crit_list.append(element[:-7])
            
            #At this point, I have the user's desired criteria and corresponding weights,
            #stored unordered in the criteria dictionary. I also have a list of events,
            #which will be used to determine the order of the returned criteria tuples
            #for each user. So the function that returns this data will use the specified order.
            #This eliminates the need to key each returned tuple.
                    
            #Now I need the data for the requested number of users
            user_data = get_user_data(crit_list, users_count)
            print(user_data)

            #now we have each user's data in the proper format
            #each tuple is ordered according to the event list
            response = CriteriaBuild(criteria)
            print('Normalized data')
            print(response.data)
            print('generate score...')
            response.generate_score(crit_list, user_data)

            #the build_chart method will handle any legit keyword for the given chart type
            kwargs = {
                'chf' : 'c,lg,0,EFEFEF,0,BBBBBB,1', #chart_colors
                'chxt' : 'x,y', #visible_axis
                'chxl' : '1:|%s' %(get_users(users_count)), #user labels
                'chbh' : 'a', #bar_width
                'chs' : '800x360', #chart_size
                'cht' : 'bhs', #chart_type
                'chco' : '80C65A,0F9E00,2C58C6,FF3030', #colors
                'chd' : 'e:MzHCHCMzGZ,DMJmHCGZTM,GZMzDMGZFH,FHHrPWI9Fw', #data
                'chdl' : 'opens|clicks|forwards|shares', #labels
                'chtt' : "Im in ur post analysing your d00ds", #title
                'chts' : '676767,19.5', #style
            }
        else: #invalid form
            kwargs = default_chart()
    
    else: #not post
        form = EngagementForm() 
        kwargs = default_chart()

    context = {
        'chart_url' : build_chart(**kwargs),
        'form' : form,
        'post_url' : '/engagement/',
        'debug' : kwargs['chd'],
    }
    
    return render_to_response('main.html', context,
               context_instance=RequestContext(request))
               