def get_profile(*, name='julian', profession='programmer'):
    '''A function that only allows 2 keyword arguments: name and profession
    which default to julian and programmer respectively.

    The function does nothing fancy, just return a str: name is a profession.
    '''
    return '{} is a {}'.format(name, profession)

#Parameters after “*” or “*identifier” are keyword-only parameters and may
#only be passed used keyword arguments!

                               


