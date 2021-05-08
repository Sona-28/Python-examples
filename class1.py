class Parent:
    def course(self):
        print("i am a parent class")

class Child(Parent):
    def course(self):
        print("i am a child class")

c1=Child()
c1.course()