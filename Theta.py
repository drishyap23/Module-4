scores = [90, 75, 88, 62, 95]

steps = 1
top_score = scores[0]
print('Score   :', top_score)
print('Steps   :', steps)
print('Theta   : Theta(1) -- best case = worst case = 1 step')


n = len(scores)
total = 0
for score in scores:
    total += score
print('Total   :', total)