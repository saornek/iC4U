#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myMotor = AFMS.getMotor(1);
Adafruit_DCMotor *myOtherMotor = AFMS.getMotor(2);

String voice;

const int buttonPin = 53;  // the number of the pushbutton pin
const int buttonPin1 = 51;
const int buttonPin2 = 49;

// variables will change:
int buttonState = 0;  // variable for reading the pushbutton status
int buttonState1 = 0;
int buttonState2 = 0;

int rainSensor = 15;
int sensorVal;
int sensortrigger = 605;

int sensor_pin = A14;
int buzzer_pin = 43;

//Sensörün çalışması için gerekli ön ısıtma süresini 5sn olarak belirliyoruz
int preheat_time = 5000;
//Alarmın çalması için gerekli eşik değerini 300 olarak belirliyoruz.
int threshold = 300;


Servo NeckServo;
Servo LegServo;

int ledleft = 31;
int ledright = 35;

void setup() {
  Serial.begin(9600);       // set up Serial library at 9600 bps
  Serial.println("1-C4U");  // initialize the pushbutton pin as an input:

  pinMode(buttonPin, INPUT);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);

  pinMode(ledleft, OUTPUT);
  pinMode(ledright, OUTPUT);

  pinMode(rainSensor, INPUT);

  //Alarm için kullanacağımız buzzer ve LED'leri çıkış olarak tanımlıyoruz
  pinMode(buzzer_pin, OUTPUT);


  NeckServo.attach(10);  // attaches the servo on pin 9 to the servo object
  LegServo.attach(9);

  AFMS.begin();  // create with the default frequency 1.6KHz
  // Set the speed to start, from 0 (off) to 255 (max speed)

  lcd.init();  // initialize the lcd
  lcd.init();
  printMessageLcd();

  myMotor->setSpeed(0);
  myOtherMotor->setSpeed(0);

  //İlk 5sn boyunca sensörün ısınmasını bekliyoruz. Bu esnada LED mavi renkte yanıyor:
  Serial.println("Sensor isitiliyor...");
  delay(preheat_time);
  //Isıma işlemi için gereken 5sn süre tamamlandığında mavi LED'i söndürüyoruz:
}

void loop() {


  checkRain();
  checkGasSensorandBuzzer();

  checkButton();
  checkVoice();
}

void forward() {
  NeckServo.write(90);
  LegServo.write(90);

  digitalWrite(31, LOW);
  digitalWrite(35, LOW);
  myMotor->run(FORWARD);
  myMotor->setSpeed(150);
  myOtherMotor->run(FORWARD);
  myOtherMotor->setSpeed(150);
}

void stopMotor() {
  myMotor->run(RELEASE);
  myMotor->setSpeed(0);
  myOtherMotor->run(RELEASE);
  myOtherMotor->setSpeed(0);
}

void backward() {

  digitalWrite(31, HIGH);
  digitalWrite(35, HIGH);
  myMotor->setSpeed(150);
  myOtherMotor->run(BACKWARD);
  myOtherMotor->setSpeed(150);
}

void left() {


  digitalWrite(35, LOW);
  digitalWrite(31, HIGH);
  myMotor->run(FORWARD);
  myMotor->setSpeed(125);
  myOtherMotor->run(FORWARD);
  myOtherMotor->setSpeed(125);
  LegServo.write(45);
  NeckServo.write(135);
  delay(2000);
}

void right() {

  digitalWrite(31, LOW);
  digitalWrite(35, HIGH);
  myMotor->run(FORWARD);
  myMotor->setSpeed(125);
  myOtherMotor->run(FORWARD);
  myOtherMotor->setSpeed(125);
  NeckServo.write(45);
  LegServo.write(135);
  delay(2000);
}

void checkButton() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:

  if (buttonState == HIGH) {
    Serial.println("p");
    myMotor->setSpeed(175);
    myOtherMotor->setSpeed(175);
    myMotor->run(FORWARD);
    myOtherMotor->run(FORWARD);

  } else if (buttonState1 == HIGH) {
    myMotor->run(RELEASE);
    myOtherMotor->run(RELEASE);
    myMotor->setSpeed(0);
    myOtherMotor->setSpeed(0);
  }

  else if (buttonState2 == HIGH) {
    myMotor->setSpeed(125);
    myOtherMotor->setSpeed(125);
  }
}

void checkVoice() {
  while (Serial.available()) {  //Check if there is an available byte to read
    delay(10);                  //Delay added to make thing stable
    char c = Serial.read();     //Conduct a serial read
    if (c == '#') {
      break;  //Exit the loop when the # is detected after the word
    }
    voice += c;  //Shorthand for voice = voice + c
  }

  if (voice.length() > 0) {
    Serial.println(voice);

    if (voice == "*go") {
      forward();
    } else if (voice == "*back") {
      backward();
    } else if (voice == "*stop") {
      stopMotor();
    } else if (voice == "*left") {
      left();
      delay(100);
      forward();
    } else if (voice == "*right") {
      right();
      delay(100);
      forward();
    }

    voice = "";
  }
}



void checkRain() {
  int sensorVal = analogRead(rainSensor);
  if (sensorVal < sensortrigger) {
    Serial.println("It is Raining!");

    delay(250);
  } else {
    Serial.println("No Rain!");

    delay(250);
  }
  delay(750);
}

void checkGasSensorandBuzzer() {
  //analogRead() fonksiyonu ile sensör değerini ölçüyoruz ve bir değişken içerisinde tutuyoruz:
  int sensorValue = analogRead(sensor_pin);
  //Sensör değeri belirlediğimiz eşik değerinden yüksek ise alarm() fonksiyonunu çağırıyoruz:
  if (sensorValue >= threshold)
    alarm(100);
  //Alarmın çalmadığı durumda LED'in yeşil yanmasını istiyoruz:
  Serial.println(sensorValue);
  //Sensör değerini bilgisayarımızdan görebilmek için seri monitöre yazıyoruz:
}

void alarm(unsigned int duration) {
  //Buzzer'ın 440Hz'te (la notası) ses üretmesini istiyoruz:
  tone(buzzer_pin, 440);
  delay(duration);
  noTone(buzzer_pin);
}