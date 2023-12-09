rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
# rock = 0
# paper = 1
# scissors = 2
hm = int(input('"0" is Rock, "1" is Paper, "2" s Scissors. Plz take you choice~ \n'))
cp = random.randint(0,2)

if hm == 0:
  print("your chose:\n" + rock)
elif hm == 1:
  print("your chose:\n" + paper)
elif hm == 2:
  print("your chose:\n" + scissors)

if cp == 0:
  print("computer chose:\n" + rock)
elif cp == 1:
  print("computer chose:\n" + paper)
elif cp == 2:
  print("computer chose:\n" + scissors)
  
if hm == cp:
  print('it\'s a tie.')
elif (hm == 0 and cp == 2) or (hm == 1 and cp == 0) or (hm == 2 and cp == 1):
  print("congrats, you won!")
else:
  print("sorry human, you lost! HAHA~")