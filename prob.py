# Introduction to Random Strings (Modeling Random Genomes)
# https://rosalind.info/problems/prob/

from math import log10


with open('data/rosalind_prob.txt') as f:
    dna = f.readline().strip()
    gc_content = list(map(float, f.readline().strip().split()))

ans = [1.0] * len(gc_content)
for bp in dna:
    for i in range(len(ans)):
        if bp == 'G' or bp == 'C':
            ans[i] *= gc_content[i] / 2
        else:
            ans[i] *= (1 - gc_content[i]) / 2

print(*(round(log10(a), 5) for a in ans))
