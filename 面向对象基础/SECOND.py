class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f"姓名{self.name}\n语文{self.chinese}\n数学{self.math}\n英语{self.english}"
s1=Student("王平",89,79,98)
print(s1)
s1.math=20
print(s1)
class EducationManagement:
    def __init__(self):
        self.studentlist=[]
    def addStudent(self,student):
        name=input("请输入学生姓名")
        for s in self.studentlist:
            if s.name==name:
                print("error")
                return 
        math=input("请输入math成绩")
        chinese=int(input("输入语文成绩"))
        english=int(input("请输入英语成绩"))
