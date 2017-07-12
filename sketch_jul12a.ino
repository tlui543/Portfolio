#include <Servo.h>
#define NOTE_D4 293.66
#define NOTE_E4 329.63
#define NOTE_F4 369.99
#define NOTE_A4 466.16
#define NOTE_B4 493.88
#define NOTE_C5 554.37
#define NOTE_D5 587.33
#define NOTE_E5 659.25
#define NOTE_F5 739.99
 


int speakerPin = 8;
// notes for melody
int melody[] = {
  NOTE_D4, NOTE_F5, NOTE_B4, NOTE_D5, NOTE_C5, NOTE_B4, NOTE_A4, NOTE_B4,0, NOTE_B4, NOTE_C5, NOTE_D5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_F5, NOTE_D5, NOTE_F5, 
};

int noteDurations[] {
  16,16,16,16,16,16,16,1.3,4,4,4,4,16,16,4,4,4,4,4,1.3
};

Servo servoLeft;
Servo servoRight;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(13);
  servoRight.attach(12);
  pinMode(speakerPin, OUTPUT);
}

void loop() {
//  servoLeft.writeMicroseconds(1700); //left wheel, robot is going clockwise
//  servoRight.writeMicroseconds(1300); //pause
//  delay(500);
//  servoLeft.writeMicroseconds(1300); //left wheel, robot is going clockwise
//  servoRight.writeMicroseconds(1700); //pause
//  delay(1000);  
//
//  delay(500);

  for (int thisNote = 0; thisNote < 20 ; thisNote++) {
    // Calculate note duration, take one second and divide it by the note type
    int noteDuration = 1000/ noteDurations[thisNote];
    tone(speakerPin, melody[thisNote], noteDuration);

    // pause between your notes, notes duration + 30% works
    
    int pauseBetweenNotes = noteDuration * 1.30;
 
    
    if (thisNote %3 == 0){
     servoLeft.writeMicroseconds(1700); //left wheel, robot is going clockwise
     servoRight.writeMicroseconds(1300); //pause
    
    }
    else if (thisNote %3 == 1) {
     servoLeft.writeMicroseconds(1300); //left wheel, robot is going clockwise
     servoRight.writeMicroseconds(1700); //pause
     
    }
    else if (thisNote %3 == 2){
     servoLeft.writeMicroseconds(1500); //left wheel, robot is going clockwise
     servoRight.writeMicroseconds(1300); //pause
    
    }
    delay(pauseBetweenNotes);
    noTone(speakerPin);
    
  }
  
 
}
