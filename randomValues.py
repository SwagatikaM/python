import random

for i in range(4):
    print(random.randint(10, 40))


employee = ["J", "K", "R"]
leader = random.choice(employee)
print(leader)
