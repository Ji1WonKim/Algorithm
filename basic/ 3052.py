list1 = []

for i in range(10):
  list1.append(int(input()))  
    
for li in range(10):  
  list1[li]=list1[li]%42

list1 = set(list1)

print(len(list1))
