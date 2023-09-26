from random import randint 


def check(comp, user):
 if comp== user:
   return 0
 if comp==0 and user== 2:
  return -1
 if comp==1 and user== 0:
  return -1
 if comp==2 and user== 1:
  return -1
 return 1

def num_to_input(x):
  if x==0:
    print("Rocks")
  elif x==1:
    print("Paper")
  elif x==2:
    print("Scissors")

def logic():
  score= 0
  comp= randint(0,2)
  print("\nYour input?")
  user= input("\033[1;32m(r for Rock, p For Paper, s for scissors:)  ")
  if user=="r":
    user= 0
  elif user=="p":
    user=1
  elif user=="s":
    user=2
  winner= check(comp,user)
  print("\nComputer Chooses:") 
  num_to_input(comp)
  print("User Chooses:")
  num_to_input(user)
  if winner==0:
   print(" \nComputer choses the same, that's a draw") 
   logic()
  elif winner== -1:
   print("\nthe computer got you, that's a lose!")
   print(f"Your Score Is {score}")
  elif winner== 1:
   print("\nok humans are better than computer, anyway you won!")
   logic()
   score= score + 1
logic()

  
 
  





