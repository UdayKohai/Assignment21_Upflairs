# Q1
# Multiple 
class Mother:
    def __init__(self) -> None:
        self.M_name = input("Enter Mother's Name : ")
    def dis(self):
        print(f"Mother Name : {self.M_name}")

class Father:
    def __init__(self) -> None:
        self.F_name = input("Enter Father's Name : ")
    def dis(self):
        print(f"Father Name : {self.F_name}")

class Child(Father, Mother):
    def __init__(self) -> None:
        Mother.__init__(self)
        Father.__init__(self)
        
    def show(self):
        Mother.dis(self)
        Father.dis(self)

obj1 = Child()
obj1.show()