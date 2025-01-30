class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    # pass
    def method1(self):
        print("Dog barks")

class Cat(Animal):
    pass
    def speak(self):
        print("Cat meows")

# A=Animal()
# A.speak()
# # Creating instances of Dog and Cat
dog = Dog()
cat = Cat()
#
# # Polymorphism: Both objects respond to the same method in their own way
# dog.speak()  # Outputs: Dog barks
cat.speak()  # Outputs: Cat meows






