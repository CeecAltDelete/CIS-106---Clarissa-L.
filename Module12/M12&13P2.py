lname = ["Lara","Johnson","Byrd","Ortega","Johnson III","Brady","Fitzgerald","Valenzuela","Best","Henderson"]
scores = [100,72,81,81,83,94,86,71,90,79]

def exams(lname,scores):
  for x in range(0,10,1):
    print(lname[x], "scored", scores[x])

exams(lname,scores)