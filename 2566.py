
array = [[0]*9 for i in range(9)]

for i in range(9) :
  array[i] = input().split()

for i in range(9) :
  for j in range(9) :
    array[i][j] = int(array[i][j])

maxx=[]
for i in range(9):
  maxx.append(max(array[i]))

maxxx = max(maxx)

ans = [(i, j) for i in range(9) for j in range(9) if array[i][j]==maxxx]

print(maxxx)
print(ans[0][0]+1, ans[0][1]+1)


