import random
import time
print("welcome to the talking parrot game !")
name=input("what's your name?")
print(f"hello {name}! let's talk with the parrot...")
funny_replies=[
    "Did you just say that?",
    "Huh? say thet again,my bird brain missed it !",
    "squak! i think i heard something weird",
    "hehehehe , thet's funny!",
    "I am genius parrot smarter than you",
    "Oh no ! my feathers are laughing",
    ]
while True:
    user=input("you: ")
    if user.lower()in ["bye","exit","quit"]:
        print("parrot : Bye Bye human")
        break
    else:
        print("parrot:"+user[::-1])
#Reverse your statement
        time.sleep(1)
        print("parrot:",random.choice(funny_replies))
        print()
