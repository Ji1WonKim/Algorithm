t = int(input())
li = []
for i in range(t):
    li.append(int(input()))

li.sort()

for i in range(t):
    print(li[i])
