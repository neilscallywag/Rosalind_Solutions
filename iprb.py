"""
Mendel's First Law
url: http://rosalind.info/problems/iprb/
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

import random as random

def parent(k,m,n):
    i = random.uniform(0, 1)
    if i <= (k/(k+m+n)):
        Y = ['A','A']
        k -= 1
    elif (k/(k+m+n)) <= i <= (1 - (n/(k+m+n))):
        Y = ['A','a']
        m -= 1
    else:
        Y = ['a','a']
        n -= 1
    return f1(k,m,n,Y)

def f1(k,m,n,Y):
    i = random.uniform(0, 1)
    if i <= (k/(k+m+n)):
        X = ['A','A']
    elif (k/(k+m+n)) <= i <= (1 - (n/(k+m+n))):
        X = ['A','a']      
    else:
        X = ['a','a']
    return list(random.choice(X)) + list(random.choice(Y))


    
def prob(k,m,n):
   counter = 0
   r = 1000
   for i in range(r):
       q = parent(k,m,n)
       if ('A' in q ):
           counter += 1          
       else:
           counter +=0         
   return (counter/r)
   
print(prob(2,2,2))
    
   
 
