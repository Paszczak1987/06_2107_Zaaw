class ClassA:
    description = "This is ClassA"
    id = 1
    
    def __init__(self, name):
        self.name = name
        self.id = ClassA.id
        ClassA.id += 1
    
    def __str__(self):
        return f"{self.id}: {self.name}"
    
    @classmethod
    def introduction(cls):
        print(cls.description)


class ClassB(ClassA):
    description = "This is ClassB"
    
    def __init__(self, name):
        super().__init__(name)


objA = ClassA("object of ClassA")
objB = ClassB("object of ClassB")
objB_2 = ClassB("object of ClassB")

print(objA)
print(objB)
print(objB_2)
