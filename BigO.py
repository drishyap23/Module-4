names = ['Aarav', 'Priya', 'Dev', 'Meera', 'Kabir']
n = len(names)

target = 'Kabir'
steps  = 0
for name in names:
    steps += 1
    if name == target:
        break

print('Target   :', target)
print('Steps    :', steps, '(worst case = n =', n, ')')
print('Big-O    : O(n)')