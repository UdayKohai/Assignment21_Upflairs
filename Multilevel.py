# Q1
# Multilevel
class GF:
    def __init__(self) -> None:
        self.grand_father_name = input("Enter your Grand Father name : ")
        
class F(GF):
    def __init__(self) -> None:
        self.father_name = input("Enter your Father name : ")

class K(F):
    def __init__(self) -> None:
        self.name = input("Enter your name : ")
        F.__init__(self)
        GF.__init__(self)
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Father Name : {self.father_name}")
        print(f"Grand Father Name : {self.grand_father_name}")


obj = K()
obj.display()
    