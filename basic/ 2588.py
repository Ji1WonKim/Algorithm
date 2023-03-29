a = int(input())
b = int(input())

n3 = a * (b%10)
n4 = a * ((b//10)%10)
n5 = a * (b//100)
n6 = n3 + n4*10 + n5*100

print(n3, n4, n5, n6, sep="\n")
