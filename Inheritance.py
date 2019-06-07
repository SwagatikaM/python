class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    #pass
    def bark(self):
        print("bark")


class Cat:
    #pass
    def meow(self):
        print("meow")


dog = Dog()
dog.bark()
dog.walk()


cat = Cat()
cat.meow()