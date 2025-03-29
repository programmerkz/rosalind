# Translating RNA into Protein
# https://rosalind.info/problems/prot/

from typing import Generator


RNA_CODONS = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S',
    'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y',
    'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L',
    'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
    'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I',
    'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T',
    'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
    'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A',
    'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
    'GGG': 'G',
    'UGA': 'Stop', 'UAA': 'Stop', 'UAG': 'Stop',
}

STOP_CODONS = {'UGA', 'UAA', 'UAG'}


def triplets_generator(s: str, stoppable: bool = True) -> Generator[str, None, None]:
    for i in range(len(s) // 3):
        triplet = s[i * 3: (i + 1) * 3]

        if stoppable and triplet in STOP_CODONS:
            break
        else:
            yield triplet


with open('data/rosalind_prot.txt') as f:
    rna = f.readline().strip()

protein = ''.join(RNA_CODONS[triplet] for triplet in triplets_generator(rna))
print(protein)
