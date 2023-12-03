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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
gender = input("please input your gender. \n")
move = input("choose left or right to go. \n")
action = 0

if move == "left" or move == "L" or move == "LEFT":
  action = input("do you wanna wait or swim? \n")
else:
  key = input("could you find the key? \n")

if action == "wait" or "WAIT":
  colour = input("whats your fav colour? \n")
  if colour == colour:
    print(f"congrats, this {colour} crystal is yours!")
else:
  swim = input("can you swim to the bottom of the lake? \n")
  if swim == "Y" or swim == "Yes" or swim == "yes":
    if gender == "m" or gender == "M" or gender == "male" or gender == "MALE":
        print("congrats, i would turn u into a strong merman!")
    else:
        print("congrats, i would turn u into a beautiful mermaid!")
if key == "y" or key == "Y" or key == "YES" or key == "yes":
    print("sorry, that is the false key. you lost.")
else: 
    print("bye bye.")