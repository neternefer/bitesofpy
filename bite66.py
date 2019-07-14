from itertools import islice

def running_mean(sequence, n=1):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
##    running = []
##    answer = []
##    for  s in sequence:
##        running.append(s)
##        avg = sum(running)/len(running)
##        answer.append(round(avg, 2))
##    print(answer)
    for sel in win(sequence, size):
        yield sum(sel) / size
                   

def win(seq, n=1):   
     it = iter(sequence)
     result = tuple(islice(it, n))
     if len(result) == 1:
         yield result
     for elem in it:
         result = result[1:] + (elem, )
         yield result
    
running_mean([1, 2, 3])
