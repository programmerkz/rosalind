# Finding a Motif in DNA
# https://rosalind.info/problems/subs/

from typing import Generator


def substr_generator(s: str, t: str) -> Generator[int, None, None]:
    start = 0
    while (pos := s.find(t, start)) != -1:
        start = pos + 1
        yield pos + 1


with open('data/rosalind_subs.txt') as f:
    s = f.readline().strip()
    t = f.readline().strip()

print(*substr_generator(s, t))
