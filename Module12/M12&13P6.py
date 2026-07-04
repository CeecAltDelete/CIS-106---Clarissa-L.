f = open("bat.txt","r")
pname = []
bavg = []
player = f.readline()

while player != "":
  pname.append((player).rstrip("\n"))
  b = float(f.readline())
  bavg.append(b)
  player = f.readline()
f.close()
l = len(pname)

def display (player,bavg):
  for z in pname,bavg:
    print(z)

def search(pname,player,bavg,psearch):
  for y in range(0,l,1):
    if pname[y] in psearch:
      sindex = y
      print(pname[sindex]," batting average: ",bavg[sindex])

display(player,bavg)  

response = (input("Search for another player? Input Yes or No."))
while response.lower() == "yes":
  psearch = (input("Which player?"))
  search(pname,player,bavg,psearch)
  
  response = (input("Search for another player? Input Yes or No."))