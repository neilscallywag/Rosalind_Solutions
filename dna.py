"""
Counting DNA Nucleotides
url: http://rosalind.info/problems/dna/
Given: A DNA string  of length at most 1000 nt
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in
"""

def c_n(x):
    a = x.count("A")
    c = x.count("C")
    g = x.count("G")
    t = x.count("T")
    return a,c,g,t

print(c_n(str("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")))

    
