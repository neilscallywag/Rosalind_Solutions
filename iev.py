"""
Calculating Expected Offspring
url: http://rosalind.info/problems/iev/
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""

def calculate_offspring(l):
    offspring = (1*l[0] + 1*l[1] + 1*l[2] + 0.75*l[3] + 0.5*l[4] + 0*l[5]) * 2
    return offspring 
    
print(calculate_offspring(["1","0","1","1","0","1"]))
 
