"""
The Wright-Fisher Model of Genetic Drift
url: http://rosalind.info/problems/wfmd/
Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).

Return: The probability that in a population of N diploid individuals initially possessing m copies of a dominant allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model."""

#since the number of dom alleles in 1 individuak follows ~B(2N,p)where p = m/2N
from math import factorial as f
import random as r
def a(N,m,g,k):
    c = 0
    pr = 1 - ((f(N))/(f(2*N-m)*f(m)))

    for i in range(N): #calling x N times to generate alleles for N individuals
        x = r.randint(0,2*N)
        c += x
        p = ((f(N))/(f(2*N-x)*f(x)))
    return c, p #No of dominant alleles after N generation.
   
        
print(a(4,6,2,1))



def bern(p):
    i = r.uniform(0,1)
    if(i<p):
        return 1
    return 0

def sizeDoms(N,p):
    counter = 0
    for i in range(2*N - 1):
        if(bern(p) == 1):
            counter += 1
    return counter

def generation(N,m,p,g):
    for i in range(g-1):
        m = sizeDoms(N,p)
        p = m / (2*N)
    return m

counter = 0
for i in range(1000):
    if(generation(4,6,(6/2*4),2) >= 1):
        counter += 1
print(counter/1000)
    
