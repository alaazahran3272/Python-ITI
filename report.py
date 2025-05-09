
##--1--- Multiple Inheritance
## How super Function handle Multiple Inheritance.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):  # Multiple inheritance
    def show(self):
        print("D")
        super().show()

d = D()
d.show()
#
#   that is what happen    #
#d.show() calls D.show(), prints "D", then super().show() moves to next class → B
# B.show() prints "B", then super().show() goes to C
# C.show() prints "C", then super().show() goes to A
# A.show() prints "A" and stops (no super() here)
#_______________________________________________________________#
###how python will handle this 

class Human:
    def eat(self):
        print("Human eats with utensils.")

class Mammal:
    def eat(self):
        print("Mammal eats with mouth.")

class Employee(Human, Mammal):
    pass

e = Employee()
e.eat()
######################
#it will call employee class Employee and Since Human comes before Mammal, Human.eat() is used.