# 1 < x < y
# x + y <= 100
import sympy

from prettytable import PrettyTable
x = PrettyTable()


prods = {}

count = 0
# create all products
for x in range(2, 100):
    for y in range(x + 1, 100):
        s = x + y

        if s > 100:
            continue

        count += 1

        p = x * y

        if p not in prods:
            prods[p] = {
                "count": 0,
                "combinations" : []
            }

        prods[p]["count"] += 1
        prods[p]["combinations"].append((x, y))

print("Onmogelijke Puzzel")
print(f"Totaal aantal x, y combinaties: {count}")

# find all combinations that create a unique product
unique_products = set()
non_unique_product_combinations = set()
count = 0
for p in prods:
    if prods[p]["count"] == 1:
        unique_products.add(prods[p]["combinations"][0])
    else:
        count += 1
        non_unique_product_combinations.add(prods[p]["combinations"][0])

print("P zegt: 'Ik weet niet wat x en y zijn.'")

print(f"Aantal combinaties zonder uniek product: {len(non_unique_product_combinations)}")

# print(unique_products)

sums = {}
# now find all possible sums, and if they can be created with a unique combination
# create all products
for x in range(2, 100):
    for y in range(x + 1, 100):
        s = x + y

        if s > 100:
            continue

        if s not in sums:
            sums[s] = {
                "count": 0,
                "combinations" : [],
                "unique_prods": 0

            }

        sums[s]["count"] += 1
        sums[s]["combinations"].append((x, y))
        if (x, y) in unique_products:
            sums[s]["unique_prods"] += 1

print("S zegt: 'Dat wist ik al.'")

# find all sums that cannot be created with a unique product combination
combinations_with_sums_that_can_only_be_created_with_non_unique_products = set()
print("Sommen die alleen gemaakt kunnen worden met combinaties die geen uniek product opleveren:")
for s in sums:
    if sums[s]["unique_prods"] == 0:
        print(s, end=" ")
        combinations_with_sums_that_can_only_be_created_with_non_unique_products = combinations_with_sums_that_can_only_be_created_with_non_unique_products.union(set(sums[s]["combinations"]))
print(f"({len(combinations_with_sums_that_can_only_be_created_with_non_unique_products)} combinaties)")

sum_prods = {}
for x, y in combinations_with_sums_that_can_only_be_created_with_non_unique_products:
    p = x * y

    if p not in sum_prods:
        sum_prods[p] = {
            "count": 0,
            "combinations": []
        }

    sum_prods[p]["count"] += 1
    sum_prods[p]["combinations"].append((x, y))

print("P zegt: 'Nu weet ik het wel.'")
print(f"Aantal producten dat daarmee mogelijk is {len(sum_prods)}.")

unique_sum_prods = set()
for p in sum_prods:
    if sum_prods[p]["count"] == 1:
        unique_sum_prods = unique_sum_prods.union(set(sum_prods[p]["combinations"]))

print(f"Aantal unieke producten daarvan {len(unique_sum_prods)}.")


print("Unieke producten per som:")
x = y = None
for s in sums:
    if sums[s]["unique_prods"] == 0:
        solutions = unique_sum_prods.intersection(set(sums[s]["combinations"]))
        print(f"{s} ({len(solutions)})", end=" ")
        if len(solutions) == 1:
            x, y = list(solutions)[0]

print()
print("S zegt: 'Dan weet ik het nu ook.'")

print(f"Antwoord: x = {x}, y = {y}")


#
#         if s not in sums:
#             sums[s] = {
#                 "count": 0,
#                 "two_primes": 0
#             }
#
#         if sympy.isprime(x) and sympy.isprime(y):
#             sums[s]["two_primes"] += 1
#         sums[s]["count"] += 1
#
#
# legal_sums = list(sums.keys())
# legal_sums.sort()
#
# x = PrettyTable()
#
# x.field_names = ["Sum", "Count", "NoPrimes", "Found"]
#
# sum_of_no_primes = set()
#
# for key in legal_sums:
#     x.add_row([key, sums[key]["count"], sums[key]["count"] - sums[key]["two_primes"], sums[key]["two_primes"] == 0])
#
#     if sums[key]["two_primes"] == 0:
#         print(f"Sum can be: {key}")
#         sum_of_no_primes.add(key)
# print(x)
#
# prods = {}
#
# count = 0
# for x in range(2, 100):
#     for y in range(x + 1, 100):
#         s = x + y
#         p = x * y
#
#
#         if p not in prods:
#             prods[p] = {
#                 "combinations": [],
#                 "sum_of_no_primes": 0
#             }
#         prods[p]["combinations"].append((x, y))
#         if s in sum_of_no_primes:
#             prods[p]["sum_of_no_primes"] += 1
#
#
# for p in prods:
#     if prods[p]["sum_of_no_primes"] == 1:
#         print(p, prods[p])
