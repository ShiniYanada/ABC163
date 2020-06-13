n = int(input())
datas = [int(i) for i in input().split()]
outputs = [0] * n
for i in datas:
  outputs[i - 1] += 1
for i in outputs:
  print(i)
