import time
from playsound import playsound

print("------Pendulum clock------\n")

print("Time: "+time.strftime("%I : %M : %S")+"\n")

time.sleep(2)

print("tick tock tick ...\n")

time.sleep(2)

print("Minimize the window for your convinence and forget :)\n")

time.sleep(2)

print("tick tock tick ...")

tm = int(time.strftime("%M"))

# to halt the program
if(tm<29 and tm>=0):
    time.sleep(29-tm)
elif(tm<58 and tm>=30):
    time.sleep(59-tm)

while(True):
    curr_min = int(time.strftime("%M")) # get current minute reading    
    
    # at every hour
    if(curr_min==0):
        i = int(time.strftime("%I")) # get current hour reading
    
        # play sound according to hours
        while(i): 
            playsound('hours.wav')
            i = i-1
    
        time.sleep(29-curr_min) #halt
    
    # at every half hour
    elif(curr_min==30):
        playsound('half.wav')
        time.sleep(59-curr_min) #halt   
