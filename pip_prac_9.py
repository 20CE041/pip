class Student:
    def __init__(self, name, num):
        self.rollno = num
        self.name = name
    
class Exam(Student):
    def __init__(self,name,num,marks):
        Student.__init__(self,name,num)
        self._marks = marks

class Result(Exam):
    def __init__(self,name,num,marks):
        Exam.__init__(self,name,num,marks)
        self.total_marks = sum(marks)
        self.percentage = (self.total_marks/90)*100
    
    
    def display(self):
        print(f"{self.name} has secured {self.total_marks} and {self.percentage}%")
    
       
s1 = Result('Himani',1,[25,20,18])
s2 = Result('Jay',2,[30,25,20])
s3 = Result('Pranay',3,[25,30,25])
s4 = Result('Jiya',4,[25,25,25])
s5 = Result('prutha',5,[25,20,20])

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()