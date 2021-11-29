import json
import FIRST
import FOLLOW

# INPUT
n = int(input())
productions = {}
for i in range(0, n):
    inpPro = input()
    inpPro = list(inpPro.split("->"))
    productions[inpPro[0]] = list(inpPro[1].split("|"))

# Finding First
first = FIRST.First(productions)
# Finding follow
follow = FOLLOW.Follow(productions, first)

# OUTPUT
print("First and follow for the Non terminals are:")
for i in productions:
    print(i, " --- ", "First:", first[i], "Follow: ", follow[i])