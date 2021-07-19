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

def newF1(k,m,n):   
    o = list(random.choice(helper(k,m,n)))
    p = list(random.choice(helper(k,m,n)))
    f1 = o + p
    return f1
    
def prob(k,m,n):
   counter = 0
   r = 100000
   for i in range(r):
       q = newF1(k,m,n)
       if ('A' in q ): 
           counter += 1          
       else:
           counter +=0         
   return (counter/r)
   
  
print(prob(2,2,2))
    
   
 
