


import sys
import math
totalsize = 0 # file size
total = 0 # Entropy
lis = [0] * 256
for char in sys.stdin.read(): # count characters
  char = ord(char)
  lis[char] += 1
  totalsize += 1
for a in range(len(lis)):#calculating entropy
  if lis[a] != 0:
    h = lis[a]/totalsize * math.log2(lis[a]/totalsize)
    total += h
print (-total)
