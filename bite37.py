def countdown_for(start=10):
    '''Rewrite a simple countdown loop using recursion'''
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    print(start)
    if start > 1:
        countdown_recursive(start-1)
    else:
        print('time is up')



countdown_recursive(start=10)       


