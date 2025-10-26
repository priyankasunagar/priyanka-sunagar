#"who want's to be a millionarie?"

print("welcome to who wants to be a millionarie!")
print("lets begin the game!\n")

#Qustion no 1

print("Qustion no 1 : which company created a programing language python ?")
print("options:")
companies= ['microsoft','google','none','flipkart']
for company in companies:
    print(company)
answer=input("enter your answer: ").lower()
if answer == "none":
    print("correct answer you won one crore rupees ! !")
else:
    print ("sorry ! you lose one crore rupees")

#qustion number 2

print("Qustion no 2:what will be the output of(2**3)?")
print("options")
options=['8','6','5','3']
print(options)
answer=input("enter your answer:").lower()
if answer == "8":
    print ("you won 10 crore rupees ! !")
else :
    print("sorry ! , better luck next time ")
