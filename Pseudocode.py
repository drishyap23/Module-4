# Pseudocode - sum of first n numbers:
# INPUT n
# total = 0
# FOR each number FROM 1 TO n:
#     total = total + number
# OUTPUT total

# The same logic in Python:
n = 4
total = 0
for number in range(1, n + 1):
    total += number
print(total)   # Output: 10