
num = list(map(str, input()))
b = []

for i in num:
    a = i.replace("9", "6")
    b.append(a) 

num = list(map(int, b))

c = num.count(6)

if c>0:
    for i in range(c//2):
        num.remove(6)

dict = {}

for i in num: 
    if i in dict: 
        dict[i]+=1
    else: dict[i]=1

dict.items()
a = sorted(dict.items(), key=lambda x: x[1], reverse=True)

print(a[0][1])