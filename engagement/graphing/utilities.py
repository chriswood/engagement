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

   