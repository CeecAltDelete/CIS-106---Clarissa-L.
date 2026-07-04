f = open("sample.txt","r")
last = []
score = []
lname = f.readline()

while lname != "":
  last.append(str(lname).rstrip("\n"))
  s = str(f.readline())
  score.append(s)
  l = f.readline()
  
f.close()
l = len(last)

def display(lname,score):
  for z in last,score:
    print (z)

def high(lname,score):
  high_var = -1
  for x in (0,l,1):
    if float(score[x]) > float(high_var):
      high_index = x
      high_var = score[x]

  print(last[high_index]," has the highest score of ", score[high_index])

def low(lname,score):
  low_var = 999
  for y in (l,0,-1):
    if float(score[y])<float(low_var):
      low_index = y
      low_var = score[y]
  print(last[low_index]," has the lowest score of ",score[low_index])

display(lname,score)
high(lname,score)
low(lname,score)