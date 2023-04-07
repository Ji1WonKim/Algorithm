li = []

li = list(map(str, input()))
li = list(map(int, li))
li.sort(reverse=True)
li = list(map(str, li))


lis = ''.join(li)
print(lis)

