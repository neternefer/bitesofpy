INDENTS = 4

poem = '''
          Remember me when I am gone away,
          Gone far away into the silent land;
          When you can no more hold me by the hand,

          Nor I half turn to go yet turning stay.

          Remember me when no more day by day
          You tell me of our future that you planned:
          Only remember me; you understand'''

p = """
    To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer

    The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
    """


def print_hanging_indents(poem):
    '''
    Print out formatted poem, taking care of hanging indents
    '''
    b = poem.split('\n')
    for i in range(len(b) - 1):
        if b[i] == '':
            print(b[i + 1].strip())
        else:
            if b[i + 1] != '':
                print('    ' + b[i + 1].strip())

print_hanging_indents(poem)
        
    
 
