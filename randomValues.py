import random

for i in range(4):
    print(random.randint(10, 40))


employee = ["J", "K", "R"]
leader = random.choice(employee)
print(leader)

#Example
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
