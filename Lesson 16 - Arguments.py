def cube (number):
    return number*number*number
    
def by_three (number):
    if number%3 == 0:
        print('Cube of a number.', cube(number))
    else:
        print('Number not divisible by 3.')
a = int(input('Select a number - '))
by_three (a)