from itertools import combinations, chain
x = [1, 2, 3, 4]
subsets = [v for a in range(len(x)) for v in combinations(x, a)]
for i in range(len(subsets)//2 + 1):
    print(list(chain(subsets[i])), ' ', [e for e in x if e not in subsets[i]])