from urllib import urlencode
from math import floor
import string

def build_chart(**kwargs):
    """
        Allows you to pass in any arguments supported by google in a dictionary
        and this puts them together with base argument(s).
    """
    base = 'http://chart.apis.google.com/chart?'
    return base + urlencode(kwargs) 

    #example 'http://chart.apis.google.com/chart?chf=c,lg,0,EFEFEF,0,BBBBBB,1\
    # &chxl=1:|User1|User2|User3|User4|User5&chxt=x,y&chbh=a&chs=800x360\
    # &cht=bhs&chco=80C65A,0F9E00,2C58C6,FF3030&chd=e:MzHCHCMzGZ,DMJmHCGZTM,GZMzDMGZFH,FHHrPWI9Fw\
    # &chdl=opens|clicks|forwards|shares&chtt=Im+in+ur+response%2C+analysing+your+d00ds&chts=676767,19.5'
    
def EE_convert(number):
    '''
        converts base10 integers into google's extended encoding
    '''
    #If we get a bad value send back a "missing" character
    try:
        number = int(round(number))
    except TypeError:
        return '__'

    EXTENDED_MAP = string.ascii_uppercase + string.ascii_lowercase + ''.join([str(n) for n in range(10)]) + '-.'
    EXTENDED_MAP_LENGTH = len(EXTENDED_MAP);

    if number > (pow(EXTENDED_MAP_LENGTH, 2) - 1):
        #exceeded this encoding's capacity
        encoded_num = ".."
    elif number < 0:
        encoded_num =  '__';
    else:
        quotient = int(floor(number / EXTENDED_MAP_LENGTH))
        remainder = number - EXTENDED_MAP_LENGTH * quotient
        encoded_num = EXTENDED_MAP[quotient] + EXTENDED_MAP[remainder]

    return encoded_num
    
def get_user_data(events, user_count):
    '''
        This represents returned data. for each user, you have a list of tuples.
        Each tuple represents some event (mailing for instance). Each item in the tuple
        stores whether they performed a particular criteria. The order of these will be determined
        by the events list. The query will probably want to return top or bottom users
    '''
    #{'forwards', 'opens', 'shares', 'clicks'}
    
    return {
        'user1' : [(1,1,1,1), (1,1,1,1), (1,1,1,1), (1,1,1,1), (1,1,1,1)],
        'user2' : [(1,0,0,0), (1,0,0,0), (1,0,0,0), (1,0,0,0), (1,0,0,0)],
        'user3' : [(1,1,0,0), (1,0,1,0), (1,1,1,0), (0,0,0,0), (0,0,0,0)],
        'user4' : [(1,0,0,1), (1,0,0,1), (1,0,0,0), (1,0,0,1), (1,0,0,0)],
        'user5' : [(0,1,0,0), (0,1,0,0), (0,1,0,0), (1,1,1,0), (1,1,1,0)],
    }
    
def get_users(user_count):
    '''
        stubbed in to set up users whose response data we want
    '''
    return('|'.join(['user%s' %(str(x)) for x in range(1, user_count + 1)]))
    
def format_data(data):
    """
        takes the dictionary from returned response data and
        formats it for google chart usage
    """
    return data
    
def default_chart():
    """
        This should be something fancy looking to show when there is no
        available data or to give the user an idea of what this is about.
    """
    return {
        'chf' : 'c,lg,0,EFEFEF,0,BBBBBB,1', #chart_colors
        'chxt' : 'x,y', #visible_axis
        'chxl' : '1:|Colt|Howie|Terry|Jodie|Chevy', #y axis
        'chbh' : 'a', #bar_width
        'chs' : '800x360', #chart_size
        'cht' : 'bhs', #chart_type
        'chco' : '80C65A,0F9E00,2C58C6,FF3030', #colors
        'chd' : 'e:MzHCHCMzGZ,DMJmHCGZTM,GZMzDMGZFH,FHHrPWI9Fw', #data
        'chdl' : 'opens|clicks|forwards|shares', #labels
        'chtt' : "Im in ur response analysing your d00ds", #title
        'chts' : '676767,19.5', #style
    }


   