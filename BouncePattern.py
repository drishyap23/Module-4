print("Bounce Pattern")
def inc_dec(n):
  if n==0:
    return 0
  print(n)
  inc_dec(n-1)
  print(n)
inc_dec(5)