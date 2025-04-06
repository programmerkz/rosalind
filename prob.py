# Introduction to Random Strings (Modeling Random Genomes)
# https://rosalind.info/problems/prob/

from math import log10


with open('data/rosalind_prob.txt') as f:
    dna = f.readline().strip()
    gc_content = list(map(float, f.readline().strip().split()))

GC = sum(bp in 'GC' for bp in dna)
AD = len(dna) - GC

dna_prob = lambda prob: log10((prob / 2) ** GC * ((1 - prob) / 2) ** AD)

ans = [round(dna_prob(prob), 5) for prob in gc_content]
print(*ans)
