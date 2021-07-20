"""
Transcribing DNA into RNA 
url: http://rosalind.info/problems/rna/
Given: A DNA string  having length at most 1000 nt.
Return: The transcribed RNA string of .
"""

def transcription(x):
    return x.replace("T","U")

print(transcription(str("GATGGAACTTGACTACGTAAATT")))
