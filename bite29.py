def get_index_different_char(chars):
    '''Return index of the element that doesn't fit in the list
       e.g. only alphanumeric or only non-alphanumeric
    '''
    
    alnums = []
    notals = []

    for item in enumerate(chars):
        if str(item[1]).isalnum():
            alnums.append(item)
        else:
            notals.append(item)
    
    ind = [i[0][0] for i in [alnums, notals] if len(i) == 1]
    return ind[0]
        
        
    
        
    
            
        
