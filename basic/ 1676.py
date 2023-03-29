
n = int(input())
    
a = 1
ans = 0
if n==0:
    ans=0
else:
    while (a<(n+1)):
        if (a%125==0):
            ans+=3
        elif (a%25==0):
            ans+=2
        elif (a%5==0):
            ans+=1
        a=a+1

print(ans)

