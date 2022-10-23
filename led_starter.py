from gpiozero import LED, Button
from signal import pause
from time import sleep

led1 = LED(23)
led2 = LED(24)
led3 = LED(18)
led4 = LED(25)
led5 = LED(8)
led6 = LED(7)

Mode1 = Button(2)

cnt = False
flag = 0

def find():
    global cnt
    
    cnt = not cnt
    
    if(cnt == False):
        flag = 0
        cnt = False
    else :
        flag = 1
        cnt = True
        
        

def go():
    global cnt
    
    if (cnt == False):
        
        led1.on()
        led3.on()
        led5.on()
                        
        sleep(0.5)
                        
        led1.off()
        led3.off()
        led5.off()
                        
        sleep(0.5)
                        
        led2.on()
        led4.on()
        led6.on()
                        
        sleep(0.5)
                        
        led2.off()
        led4.off()
        led6.off()
            
        sleep(0.5)
                
    else:
        
        led1.on()
        led3.on()
        led5.on()
        led2.on()
        led4.on()
        led6.on()
                        
        sleep(0.5)
                        
        led1.off()
        led3.off()
        led5.off()
        led2.off()
        led4.off()
        led6.off()
                        
        sleep(0.5)
                    
    
while 1:
    Mode1.when_pressed = find
    
    if(flag == 0):
        go()
    else :
        go()


