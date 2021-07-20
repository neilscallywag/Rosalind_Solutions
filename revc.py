""""
Complementing a Strand of DNA
url: http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
""""




def c(c):
    r = { "A": "T", "G": "C", "T": "A", "C": "G" }
    for i, j in r.items():
        strand = c.replace(i, j)
    return strand
s = 'A A A A C C C G G T'
print(c(s))
