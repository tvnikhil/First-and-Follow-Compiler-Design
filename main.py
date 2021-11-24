import FIRST
import FOLLOW

n = int(input())
productions = {}
for i in range(0, n):
    inpPro = input()
    inpPro = list(inpPro.split("->"))
    productions[inpPro[0]] = list(inpPro[1].split("|"))
print("First for the grammar is ")
first = FIRST.First(productions)
for i in first:
    print(i, ":", first[i])
print()
print("Follow for the grammar is ")
follow = FOLLOW.Follow(productions, first)
for i in follow:
    print(i, ":", follow[i])