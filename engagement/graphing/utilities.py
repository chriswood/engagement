
def build_chart(**kwargs):
    base = 'http://chart.apis.google.com/chart?'
    visible_axis = 'x,y'
    chart_url = kwargs['base'] + kwargs['chart_colors'] + kwargs['y-axis'] + visible_axis + \
    '&chxt=x,y&chbh=a&chs=800x360&cht=bhs&chco=80C65A,0F9E00,2C58C6,FF3030&chd=e:MzHCHCMzGZ,DMJmHCGZTM,GZMzDMGZFH,FHHrPWI9Fw&chdl=opens|clicks|forwards|shares&chtt=I\'m+in+ur+response%2C+analysing+your+d00ds&chts=676767,19.5'
    print(chart_url)
    return chart_url
    
    #need like chxt = visible_axis...