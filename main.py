print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("You arrived at the island unharmed")
first_choice=input("you find two paths, will you go to the left or to the right?\n").lower()
if first_choice == "left" :
  print("You were caught as a sacrifice for the dragons tribe")
  print("GAMEOVER")
  exit()
  
else:
  print("You come across 3 houses which one will will you choose?")
House=input("gryffindor, hufflepuff, slytherin\n").lower()
if House == "gryffindor":
  print("A wild bird speaking fluent English bows before you and swears eternal loyalty")
  print("The bird shows you were the treasure is hidden")
  print("The treasure seems to be protected by some ancient magic, how do you plan to open it? ")
  wtf=input("Will you use force or will you use magic\n").lower()
  if wtf == "force":
      print("your soul were sucked by that seal and you fall into a never ending void")
      print("GAMEOVER")
  else:
      print("Your current knowledge can't open the seal")
      print("you remain another 15 years on the island till you finally opened the chest")
      print("Congratulation on getting the treasure")
elif House == "hufflepuff":
  print("you find hidden magic circle that teleport you to your home, without the treasure... ")
  print("YOU GAINED NOTHING")
  print("GAMEOVER")
else:
  print("People never heard of you again, nor was your corpse found")
  print("GAMEOVER")
