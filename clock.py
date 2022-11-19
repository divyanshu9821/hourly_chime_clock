import os
import time
from playsound import playsound

#standalone function 
def title_currTime():
    os.system('cls')
    print("------Pendulum clock------\n")
    print("Time: "+time.strftime("%I : %M : %S")+"\n")

#standalone function
def tick_tock():
    time.sleep(1)
    print("tick tock tick ...\n")

def init():
   
    title_currTime()

    tick_tock()

    time.sleep(1)
    print("Minimize the window for your convinence and forget :)\n")

    time.sleep(2)

    tick_tock()

#standalone function
def init_halt():
    minute = int(time.strftime("%M"))

    # to halt the program, it helps to reduce the cpu usage
    if(minute<29 and minute>0):
        time.sleep((29-minute)*60)

    elif(minute<58 and minute>30):
        time.sleep((59-minute)*60)        

if __name__ == "__main__" :
    
    init()

    init_halt()

    while(True):
        curr_min = int(time.strftime("%M")) # get current minute reading 

        # at every hour
        if(curr_min==0):
            
            
            title_currTime()

            i = int(time.strftime("%I")) # get current hour reading
        
            # play sound according to hours
            while(i): 
                print("Ring")
                playsound('hours.wav')
                i = i-1
            
            tick_tock()   

            time.sleep(1680) #halt
        
        # at every half hour
        elif(curr_min==30):

            title_currTime()

            print("Ring")
            playsound('half.wav')

            tick_tock()

            time.sleep(1680) #halt   