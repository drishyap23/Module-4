print("TAIL RECURSION...")
def print1_n(n):
  if n>10:
    return
  print(n,end=" ")
  print1_n(n+1)

print1_n(1)