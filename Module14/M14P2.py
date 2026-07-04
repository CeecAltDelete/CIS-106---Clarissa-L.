class student:
  def __init__(self,first,last,dcode,credits):
    self.first = first
    self.last = last
    self.dcode = dcode
    if dcode == "I":
      self.tuition = credits * 250
    elif dcode == "O":
      self.tuition = credits * 500

  def fullname(self):
    return '{} {}'.format(self.first,self.last)

  def tuitionowed(self):
    return self.tuition

stu_1=student('Clarissa','Lara','O',10)
stu_2=student('Jenna','Ortega','O',15)
stu_3=student('Tom','Brady','I',10)

print("Student: ",stu_1.fullname())
print(stu_1.fullname(),":  $",format(stu_1.tuitionowed(),".2f"))
print("Student: ",stu_2.fullname())
print(stu_2.fullname(),":  $",format(stu_2.tuitionowed(),".2f"))
print("Student: ",stu_3.fullname())
print(stu_3.fullname(),":  $",format(stu_3.tuitionowed(),".2f"))