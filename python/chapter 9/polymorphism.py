#polymorphism example

class Dog():
    def Sound(self):
        print("Dog:Bark")

class Cat():
    def Sound(self):
        print("Cat:Meow")

class Cow():
    def Sound(self):
        print("Cow:Moo")

#polymorphism in action

animals=[Dog(),Cat(),Cow()]
for a in animals:
    a.Sound()

