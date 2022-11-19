import time
from playsound import playsound

switch = bool(input("Enter 1 for ON : "))

tm = int(time.strftime("%M"))

# to halt the program
if(tm<30 and tm>=0):
    time.sleep(29-tm)
elif(tm<59 and tm>=30):
    time.sleep(59-tm)

while(switch):
    curr_min = int(time.strftime("%M")) # get current minute reading    
    
    # at every hour
    if(curr_min==0):
        i = int(time.strftime("%H")) # get current hour reading
    
        # play sound according to hours
        while(i): 
            playsound('hours.wav')
            i = i-1
    
        time.sleep(29-curr_min) #halt
    
    # at every half hour
    elif(curr_min==30):
        playsound('half.wav')
        time.sleep(59-curr_min) #halt   
