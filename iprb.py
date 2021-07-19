import random as random

def helper(k,m,n):
    i = random.uniform(0, 1)
    if i <= (k/(k+m+n)):
        X = ['A','A']
    elif (k/(k+m+n)) <= i <= (1 - (n/(k+m+n))):
        X = ['A','a']      
    else:
        X = ['a','a']
    return X


def prob(k,m,n):
   o = list(random.choice(helper(k,m,n)))
   p = list(random.choice(helper(k,m,n)))
   f1 = o + p
   counter = 0
   for i in range(1000):
       if ('A' in f1):
           counter += 1
           print(counter)
   return counter
   
   
   
    
        
    
print(prob(10,2,2))
    
   
 
