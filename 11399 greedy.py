

n = int(input())
pi = list(input().split())
pi = list(map(int, pi))

pi.sort()


ans = 0

while n>0:
    ans = ans + int(pi[0])*n
    pi.pop(0)
    n=n-1

print(ans)