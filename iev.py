# Calculating Expected Offspring
# https://rosalind.info/problems/iev/


PROB = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

with open('data/rosalind_iev.txt') as f:
    nums = list(map(int, f.readline().split()))

ans = sum(2 * n * p for n, p in zip(nums, PROB))
print(round(ans, 6))
