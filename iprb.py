# Mendel's First Law
# https://rosalind.info/problems/iprb/

with open('data/rosalind_iprb.txt') as f:
    n = list(map(int, f.readline().strip().split()))

total = sum(n)
ans = 0.0

DOMINANT, HETERO, RECESSIVE = 0, 1, 2

# The probability that two organisms will produce an individual possessing a dominant allele:
mendel_prob = {
    (DOMINANT, DOMINANT): 1.0,
    (DOMINANT, HETERO): 1.0,
    (DOMINANT, RECESSIVE): 1.0,
    (HETERO, DOMINANT): 1.0,
    (HETERO, HETERO): 0.75,
    (HETERO, RECESSIVE): 0.5,
    (RECESSIVE, DOMINANT): 1.0,
    (RECESSIVE, HETERO): 0.5,
    (RECESSIVE, RECESSIVE): 0.0,
    }

for i in range(len(n)):
    p1 = n[i] / total
    for j in range(len(n)):
        if j == i:
            p2 = (n[j] - 1) / (total - 1)
        else:
            p2 = n[j]/ (total - 1)

        ans += p1 * p2 * mendel_prob[(i, j)]

print(round(ans, 6))
