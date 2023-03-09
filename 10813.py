n, m = map(int, input().split())
basket = [_+1 for _ in range(n)]

swap=0  

for _ in range(m):
  a, b = map(int, input().split())
  swap=basket[a-1]
  basket[a-1]=basket[b-1]
  basket[b-1]=swap

print(*basket)
