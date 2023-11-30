# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
love_score = 0
low_name1 = name1.lower()
low_name2 = name2.lower()
low_nameT = low_name1 + low_name2

true = low_nameT.count("t")+low_nameT.count("r")+low_nameT.count("u")+low_nameT.count("e")


love = low_nameT.count("l")+low_nameT.count("o")+low_nameT.count("v")+low_nameT.count("e")


love_score = str(true) + str(love)
x = int(love_score)

if x < 10 or x > 90:
    print(f"Your score is {x}, you go together like coke and mentos.")

elif 40 <= x <= 50:
    print(f"Your score is {x}, you are alright together.")

else:
    print(f"Your score is {x}.")