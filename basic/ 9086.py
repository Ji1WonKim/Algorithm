a = int(input())


list1 = [input() for i in range(a)]

for i in range(a):
  print(list1[i][0]+list1[i][-1])
