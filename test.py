import time
from playsound import playsound

switch = bool(input("Enter 1 for ON : "))

while(switch):
    curr_min = int(time.strftime("%M")) # get current minute reading
    
    # at every hour
    if(curr_min==51):
        i = int(time.strftime("%H")) # get current hour reading
    
        # play sound according to hours
        while(i): 
            playsound('dong.wav')
            i = i-1
    
        time.sleep(60) # halt for 60 seconds
    # at every half hour
    elif(curr_min==30):
        playsound('dong.wav')    