def fibonacci(num):
    if num == 0: 
        return 0
    
    if num == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b

def lucas(num):
    if num == 0:
        return 2
    
    if num == 1:
        return 1
    
    a, b = 2, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b

def sum_series(num, first_val = 0, second_val = 1):

    if num == 0:
        return first_val
    
    if num == 1:
        return second_val
  
    
    a, b = first_val, second_val
    for _ in range(2, num + 1 ):
        a, b = b, a + b


    return b
   


