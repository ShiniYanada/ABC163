n, m = list(map(int, input().split()))
homework = [int(i) for i in input().split()]
for i in homework:
  n -= i
if n >= 0:
  print(n)
else:
  print(-1)
