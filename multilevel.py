class Department:
   def getdeptdetails(self):
      self.id=input("enter Department id:")
      self.name=input("Enter department name:")
   def printdept(self):
      print("Depatment ID:",self.id)
      print("Department Name:",self.name)
class Course(Department):
   def getcourse(self):
      self.code=input("Enter course code:")
      self.cname=input("Enter course name:")
      self.dura=int(input("Enter duration:"))
   def printcourse(self):
      print("Course Code:",self.code)
      print("Course Name:",self.cname)
      print("Course Duration:",self.dura)
class Student(Course):
   def getdetails(self):
      self.roll=input("Enter roll no:")
      self.sname=input("Enter student name:")
      self.marks=int(input("Enter marks:"))
   def printstudent(self):
      print("\n\t---DEPARTMENT DETAILS---")
      super().printdept()
      print("\n\t---COURSE DETAILS---")
      super().printcourse()
      print("\n\t---STUDENT DETAILS---")
      print("Student Roll no:",self.roll)
      print("Student Name:",self.sname)
      print("Student Marks:",self.marks)
s=Student()
s.getdeptdetails()
s.getcourse()
s.getdetails()
s.printstudent()
