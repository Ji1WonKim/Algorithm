n = int(input())

members = []
ages = []
for i in range(n):
    member = input()
    age, name = member.split()
    age=int(age)
    members.append(member)
    ages.append(age)

n = len(ages)

for i in range(n):
    for j in range(0, n -i -1):
        if ages[j]>ages[j+1]:
            ages[j], ages[j+1] = ages[j+1], ages[j]
            members[j], members[j+1] = members[j+1], members[j]

for i in members:
    print(i)