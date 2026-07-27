class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
        print(f"{self.name}身高为{self.height},年龄为{self.age}")
    def Say_Hello(self):
        print("hello,world")
people=Person("小明",15,1.45)
people.Say_Hello()