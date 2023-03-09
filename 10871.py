
n, x = map(int, input().split())
xlist =list(map(int, input().split()))
ylist=[]
for i in range(n):
  if (xlist[i]<x):
    ylist.append(xlist[i])

print(*ylist)