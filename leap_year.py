# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
modulo1 = year % 4
modulo2 = year % 100
modulo3 = year % 400

if modulo1 == 0:
    if modulo2 == 0:
        if modulo3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")           
else:
    print("Not leap year.")