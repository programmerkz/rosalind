# Consensus and Profile
# https://rosalind.info/problems/cons/solutions/

NCL = 'ACGT'
NUCLEOTIDES = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def fasta_reader():
    with open('data/rosalind_cons.txt') as f:
        buff = []
        for id, line in enumerate(f):
            if line[0] == '>':
                if len(buff) > 0:
                    yield ''.join(buff)
                    buff = []
            else:
                buff.append(line.strip())

        if len(buff) > 0:
            yield ''.join(buff)


profile: list[list[int]] = []

for dna in fasta_reader():
    if len(profile) == 0:
        profile = [[0] * len(dna) for _ in range(4)]

    for i, nucleotide in enumerate(dna):
        profile[NUCLEOTIDES[nucleotide]][i] += 1

n = len(profile[0])
concensus = [' '] * n
for pos in range(n):
    id, seen = 0, 0
    for nucleotid_id in range(4):
        if profile[nucleotid_id][pos] > seen:
            id = nucleotid_id
            seen = profile[nucleotid_id][pos]

    concensus[pos] = NCL[id]

print(''.join(concensus))

for i in range(4):
    print(f'{NCL[i]}:', ' '.join(str(freq) for freq in profile[i]))
