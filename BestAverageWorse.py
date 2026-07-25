names = ['Aarav', 'Priya', 'Dev', 'Meera', 'Kabir']
n = len(names)

steps = 0
for name in names:
    steps += 1
    if name == 'Aarav': break
print('Best case  (Aarav):', steps, 'step   | Omega(1)')

steps = 0
for name in names:
    steps += 1
    if name == 'Dev': break
print('Average case (Dev):', steps, 'steps  | O(n)')

steps = 0
for name in names:
    steps += 1 
    if name == 'Kabir': break
print('Worst case (Kabir):', steps, 'steps  | O(n)')