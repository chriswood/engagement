from urllib import urlencode
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
    
def get_user_data(events, users):
    '''
        Stubbed in function to represent the returned data for a set of events.
        Given a set of events, and a set of users, this should return
        a matrix of dimension (len(events), len(users)) implemented via a list
        of tuples.
'''
    response_data = [
        [(1,1,1,1), (1,1,1,1), (1,1,1,1), (1,1,1,1), (1,1,1,1)],
        [(0,0,0,0), (1,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0)],
        [(1,1,0,0), (1,0,1,0), (1,1,1,0), (0,0,0,0), (0,0,0,0)],
        [(1,0,0,1), (1,0,0,1), (1,0,0,0), (1,0,0,1), (1,0,0,0)],
        [(0,0,0,0), (0,0,0,0), (0,0,0,0), (1,1,1,0), (1,1,1,0)],
    ]
    return(response_data)
    
def get_users(event_count):
    '''
        stubbed in to set up users whose response data we want
    '''
    return('|'.join(['user%s' %(str(x)) for x in range(1, event_count + 1)]))
    
def format_data(data):
    """
        takes the dictionary from returned response data and
        formats it for google chart usage
    """
    return data
    


   