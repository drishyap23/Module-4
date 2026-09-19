print("HEAD RECURSION...")
def printn(n):
  if n>10:
    return
  printn(n+1)
  print(n,end=" ")
printn(1)