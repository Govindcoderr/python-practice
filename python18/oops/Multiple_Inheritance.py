# Example of the Diamond Problem:

class A:
    def speak(self):
        print("A is speak")

class B(A):
    def speak(self):
        print("B is Speak")

class C(B):
    def speak(self):
        print("c is speak")

class D(B,C):
    def speak(self):
        pass


d = D()
d.speak()

