# 1 < x < y
# x + y <= 100
import sympy

from prettytable import PrettyTable
x = PrettyTable()

sums = {}

count = 0
for x in range(2, 100):
    for y in range(x + 1, 100):
        s = x + y

        if s > 100:
            continue

        if s not in sums:
            sums[s] = {
                "count": 0,
                "two_primes": 0
            }

        if sympy.isprime(x) and sympy.isprime(y):
            sums[s]["two_primes"] += 1
        sums[s]["count"] += 1


legal_sums = list(sums.keys())
legal_sums.sort()

x = PrettyTable()

x.field_names = ["Sum", "Count", "NoPrimes", "Found"]

sum_of_no_primes = set()

for key in legal_sums:
    x.add_row([key, sums[key]["count"], sums[key]["count"] - sums[key]["two_primes"], sums[key]["two_primes"] == 0])

    if sums[key]["two_primes"] == 0:
        print(f"Sum can be: {key}")
        sum_of_no_primes.add(key)
print(x)

prods = {}

count = 0
for x in range(2, 100):
    for y in range(x + 1, 100):
        s = x + y
        p = x * y


        if p not in prods:
            prods[p] = {
                "combinations": [],
                "sum_of_no_primes": 0
            }
        prods[p]["combinations"].append((x, y))
        if s in sum_of_no_primes:
            prods[p]["sum_of_no_primes"] += 1


for p in prods:
    if prods[p]["sum_of_no_primes"] == 1:
        print(p, prods[p])
