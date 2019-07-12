import secrets


def gen_key(parts=4, chars_per_part=8):
    '''
    Write a function called gen_key that creates a license key with this format:
    KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U. The key consists of a combination
    of upper case letters and digits.
    '''

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    key = ''
    
    for p in range(parts):
        for c in range(chars_per_part):
            key += secrets.choice(letters + numbers)
        key += '-'
    return key.rstrip('-')
        
    
 
