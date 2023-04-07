stack = []
k=int(input())
for i in range(k):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

ans = 0
for i in stack:
    ans = ans+i

print(ans)