def fizzbuzz(num):
    '''
    Replace number divisible by three with the word "Fizz", and any
    number divisible by five with the word "Buzz" or return num.
    '''
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz Buzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3== 0:
        print('Fizz')
    else:
        print(num)

fizzbuzz(15)
fizzbuzz(30)
fizzbuzz(3)
fizzbuzz(5)
 
