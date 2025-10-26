import time
t=time.strftime('%H,%M,%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter hour:"))
print(hour)
if(hour >= 0 and hour < 12):
    print("good morning sir/madam!")
elif(hour >= 12 and hour < 17):
    print("good afternoon sir /madam!")
else :
    print("good night sir / madam!")
