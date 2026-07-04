class employee:
  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@compay.com'
    self.b_rate = pay * 1.10

  def fullname(self):
    return '{} {}'.format(self.first,self.last)

  def emailaddress(self):
    return self.email

  def bonus(self):
    return self.b_rate

emp_1 = employee('Clarissa', 'Lara',10000000)
emp_2 = employee('Jenna','Ortega',75000)
emp_3 = employee('Tom','Brady',90000)

print(emp_1.fullname())
print(emp_1.emailaddress())
print("$",format(emp_1.bonus(),".2f")," is ",emp_1.fullname(), "'s salary with a 10 percent bonus.")
print(emp_2.fullname())
print(emp_2.emailaddress())
print("$",format(emp_2.bonus(),".2f")," is ",emp_2.fullname(), "'s salary with a 10 percent bonus.")
print(emp_3.fullname())
print(emp_3.emailaddress())
print("$",format(emp_3.bonus(),".2f"), " is ",emp_3.fullname(), "'s salary with a 10 percent bonus.")