#include <Servo.h>  
  
Servo frontj; 
Servo backj;
Servo ancles;
Servo neck;

int pos = 0;    
int incomingByte;    
  
void setup()  
{  
  
  Serial.begin(9600);  
    
  frontj.attach(3);
  backj.attach(4);
  ancles.attach(5);
  neck.attach(6);
  frontj.write(0);
  backj.write(0);
}  
  
void loop()  
{  
  
  if (Serial.available() > 0) {  
  
    incomingByte = Serial.read();  
  
    if (incomingByte == 'D') {    
      frontj.write(180);
      backj.write(180);
    }  
  
    if (incomingByte == 'U'){    
     
      backj.write(90);
      delay(5000); 
      frontj.write(90);
      
    } 
   if (incomingByte == 'S'){    
      
      backj.write(90);
      
    } 
   if (incomingByte == 'L'){    
      
      neck.write(45);
      ancles.write(45);
      
    } 
     if (incomingByte == 'R'){    
      
      neck.write(135);
      ancles.write(135);
  }  
  
}  
}