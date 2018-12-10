from nanpy import (ArduinoApi, SerialManager)
from time import sleep
PWM1= 3
Motor1_1= 7
Motor1_2= 4
PWM2 = 5
Motor2_1 = 8
Motor2_2 = 12
PWM3 = 6
Motor3_1 = 13
Motor3_2 = 9
def command (state):
    if state == "forward":
        
        a1 = a.analogWrite(PWM1, 255)
        print(a1)
        b1 = a.digitalWrite(Motor1_1,a.HIGH)
        c1 = a.digitalWrite(Motor1_2,a.LOW)
        a2 = a.analogWrite(PWM2, 255)
        b2 = a.digitalWrite(Motor2_1,a.HIGH)
        c2 = a.digitalWrite(Motor2_2,a.LOW)
        a3 = a.analogWrite(PWM3, 255)
        b4 = a.digitalWrite(Motor3_1,a.HIGH)
        c4 = a.digitalWrite(Motor3_2,a.LOW)
        return a1,b1,c1,a2,b2,c2,a3,b3,c3
    else:
    
        return 1
    
        
    
    
    
    
try:
    connection= SerialManager()
    a= ArduinoApi(connection=connection)
except:
    print("Failed to connect to Arduino")

a.pinMode(PWM1, a.OUTPUT)
a.pinMode(Motor1_1, a.OUTPUT)
a.pinMode(Motor1_2, a.OUTPUT)
a.pinMode(PWM2, a.OUTPUT)
a.pinMode(Motor2_1, a.OUTPUT)
a.pinMode(Motor2_2, a.OUTPUT)
a.pinMode(PWM3, a.OUTPUT)
a.pinMode(Motor3_1, a.OUTPUT)
a.pinMode(Motor3_2, a.OUTPUT)

try:
    while True:
        command("forward")
        
        
    
       
except:
    a.digitalWrite(Motor1_2, a.HIGH)
    

        
      
    
    
    
    
    
    
    
    
    
    
