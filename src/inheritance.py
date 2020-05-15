# class A: 
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C)
#     pass

# a = A()
# print(a.mro())

# print(A.__mro__)
# print(A.mro())

# print(B.mro())

# b = B()
# b.b_method()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print(f'Yum I am easting {food}')

class Tiger(Animal):
    def __init__(self, name, species, mane=False):
        super().__init__(name)

        self.species = species

    def pounce(self):
        print("You go pounced!")

class Lion(Animal):
    # def __init__(self, name, mane):
    def __init__(self, name, mane):
        super().__init__(name)

        self.mane = mane

    def roar(self):
        print("ROAR!")

class Liger(Tiger, Lion):
    def __init__(self, name, species, mane):
        super().__init__(name, species, mane)

liger = Liger("Tony", "Liger", False)
liger.pounce

# tiger = Tiger("The real tony, "Bengali", False)



