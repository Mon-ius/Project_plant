import os

from app import cli, create_app
from ext import mongo


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': mongo.db}


if __name__ =='__main__':
    app.run(host=os.getenv('IP', 'localhost'),
        port=int(os.getenv('PORT', 4444)))


import RPi.GPIO as GPIO  
import time  
import sys  

  
GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM)  
  

  
ports = [5,6,13,19,26] # GPIO 21（Pin 40） GPIO 20（Pin 38） GPIO 16（Pin 36） GPIO 19（Pin 35）  
  
for p in ports:  
    GPIO.setup(p,GPIO.OUT)  
      
for x in range(0,steps):  
    for j in arr:  
        time.sleep(0.01)  
        for i in range(0,5):  
            if i == j:              
                GPIO.output(ports[i],True)  
            else:  
                GPIO.output(ports[i],False)
for x in [0,1]:
    GPIO.output(ports[0],x)
    time.sleep(0.01) 
    for y in [0,1]:
        GPIO.output(ports[1],y)
        time.sleep(0.01) 
        for z in [0,1]:
            GPIO.output(ports[2],z)
            time.sleep(0.01) 
            for k in [0,1]:
                GPIO.output(ports[3],k)
                time.sleep(0.01) 
                for j in [0,1]:
                    GPIO.output(ports[4],j)
                    time.sleep(0.01) 