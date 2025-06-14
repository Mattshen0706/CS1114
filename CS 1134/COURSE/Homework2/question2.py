# def factors(num)
    
# # Time Complexity: O(num^0.5)

# for curr_factor in factors(100):
#     print(curr_factor)

import math 

def factors(num):
    for i in range(1,math.floor(num**0.5)):
        if num % i ==0:
            yield round(i)
        
    for i in range(math.floor(num**0.5),0,-1):
        if num % i ==0:
            yield round(num/i)
        
# for curr_factor in factors(100):
#     print (curr_factor)
