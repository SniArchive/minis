#I am lazy so i just copy pasted the same question over and over :)
questions = [
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
  ["who is the first developer of Minecraft", "steve jobs", "mojang" , "Markus (Notch)" ,"Jakob Porser" ,4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money= 0

for i in range(0,len(questions)):
  question= questions[i]
  print(f"\n\nQuestion for Rs{levels[i]}")
  print(question[0])
  print(f"\na.{question[1]}         b.{question[2]}")
  print(f"c.{question[3]}     d.{question[4]}")

  reply=int(input("Enter your answer (1-4)"))

  if(reply == question[5]):
    print(f"correct input! you have won {levels[i]}")
    if(i==4):
      money=10000
    elif(i==9):
      money=8000
    elif(i>=9):
      money="blank check! (unsigned lol)"
  else:
    print("wrong input, try again!")
    break

print("your take home money is" ,money)

