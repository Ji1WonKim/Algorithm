
#N = 총 바구니 갯수
n, m =input().split()
n=int(n)
m=int(m)
basket = list(range(1, n+1))

for i in range(m):
  a, b, c = map(int, input().split())
  a, b, c = a-1, b-1, c-1
  basket = basket[:a] + basket[c:b+1] + basket[a:c] + basket[b+1:]

print(*basket)

#모든 회전 후 가장 왼쪽에 있는 바구니부터 바구니 순서를 공백으로 구분해 출력한다.


