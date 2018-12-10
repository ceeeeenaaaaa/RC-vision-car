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
PWM4 = 10
Motor4_1 = 11
Motor4_2 = 14
    
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
        sleep(20)
        command()
        
        
    
       
except:
    a.digitalWrite(Motor1_2, a.HIGH)
    
def command (state):
    if state == "forward":
        
       return  a.analogWrite(PWM1, 255), a.digitalWrite(Motor1_1,a.HIGH),a.digitalWrite(Motor1_2,a.LOW),
               a.analogWrite(PWM2, 255), a.digitalWrite(Motor2_1,a.HIGH), a.digitalWrite(Motor2_2,a.LOW),
               a.analogWrite(PWM3, 255), a.digitalWrite(Motor3_1,a.HIGH), a.digitalWrite(Motor3_2,a.LOW),
               a.analogWrite(PWM4,255),a.digitalWrite(Motor4_1,a.HIGH), a.digitalWrite(Motor4_2,a.LOW)
    elif state == "right":
        
        return  a.analogWrite(PWM1, 255), a.digitalWrite(Motor1_1,a.LOW),a.digitalWrite(Motor1_2,a.HIGH),
                a.analogWrite(PWM2, 255), a.digitalWrite(Motor2_1,a.HIGH), a.digitalWrite(Motor2_2,a.LOW),
                a.analogWrite(PWM3, 255), a.digitalWrite(Motor3_1,a.LOW), a.digitalWrite(Motor3_2,a.HIGH),
                a.analogWrite(PWM4, 255),a.digitalWrite(Motor4_1,a.HIGH), a.digitalWrite(Motor4_2,a.LOW)
    
    elif state == "left":
        return  a.analogWrite(PWM1, 255), a.digitalWrite(Motor1_1,a.HIGH),a.digitalWrite(Motor1_2,a.LOW),
                a.analogWrite(PWM2, 255), a.digitalWrite(Motor2_1,a.LOW), a.digitalWrite(Motor2_2,a.HIGH),
                a.analogWrite(PWM3, 255), a.digitalWrite(Motor3_1,a.HIGH), a.digitalWrite(Motor3_2,a.LOW),
                a.analogWrite(PWM4,255),a.digitalWrite(Motor4_1,a.LOW), a.digitalWrite(Motor4_2,a.HIGH)
    elif state == "left":
        return  a.analogWrite(PWM1, 255), a.digitalWrite(Motor1_1,a.LOW),a.digitalWrite(Motor1_2,a.HIGH),
               a.analogWrite(PWM2, 255), a.digitalWrite(Motor2_1,a.LOW), a.digitalWrite(Motor2_2,a.HIGH),
               a.analogWrite(PWM3, 255), a.digitalWrite(Motor3_1,a.LOW), a.digitalWrite(Motor3_2,a.HIGH),
               a.analogWrite(PWM4,255),a.digitalWrite(Motor4_1,a.LOW), a.digitalWrite(Motor4_2,a.HIGH)
    else:
        print("No such command")
        return0
        
        
      
    
    
    
    
    
    
    
    
    
    
