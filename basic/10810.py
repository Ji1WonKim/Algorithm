n, m = map(int, input().split())
basket = []

for _ in range(n):  #m번 반복
  basket.append(int(0))
#i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다. 
for _ in range(m):  #m번 반복
  i, j, k = map(int, input().split())
  for ss in range((j)):
    if (ss>=(i-1)):
      basket[ss] = k 
      
print(*basket)
