import random


for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


members = ['John', 'Mary', 'Bob', 'Fahad']
leader = random.choice(members)
print(leader)
