//Lab6_M5Stick_BLE.ino
//Sample program, to run in the M5Stick, to test BLE comunication with the RPI
//v100 - PV - AAI(23/24)

// button A -  sent menssage with all MPU data
// button B - starts continuous aquisition at 10 Hz of accelarometers

#include <M5StickCPlus.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <BLE2902.h>


// See the following for generating UUIDs version 4:
// https://www.uuidgenerator.net/
//this is what identifies your M5Stick. Must be personalized
#define DEVICE_NAME         "M5-STICK-01"
#define SERVICE_UUID        "94039c15-338f-4297-9014-aaba7d760713"
#define CHARACTERISTIC_UUID "94039c15-338f-4297-9014-aaba7d760713"

BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristic = NULL;
bool deviceConnected = false;


//Globals Variables
float accX = 0.0F;
float accY = 0.0F;
float accZ = 0.0F;

float gyroX = 0.0F;
float gyroY = 0.0F;
float gyroZ = 0.0F;

float pitch = 0.0F;
float roll  = 0.0F;
float yaw   = 0.0F;

float temp = 0.0F;

bool acq_flag = false;
long acq_time = millis();
uint acq_n_samples = 0;
uint acq_samples_aquired = 0;
uint acq_sample_rate = 10;


//Callback on connection
class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      M5.Lcd.println("BLE connect");
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      pCharacteristic->setValue("Disconnected!");
      pCharacteristic->notify();
      M5.Lcd.fillScreen(BLACK);
      M5.Lcd.setCursor(0, 0); 
      M5.Lcd.println("BLE disconnect");
      deviceConnected = false;
      BLEAdvertising *pAdvertising = pServer->getAdvertising();
      pAdvertising->start();
      M5.Lcd.println("BLE running.");
    }
};

//Callback to read and write messages
class MyCallbacks: public BLECharacteristicCallbacks {
  void onRead(BLECharacteristic *pCharacteristic) {
    M5.Lcd.println("Tx to RPI");
    pCharacteristic->setValue("Message from M5Stick");
  }
  
  void onWrite(BLECharacteristic *pCharacteristic) {
    String stmp;

    M5.Lcd.println("Rx from RPI");
    std::string value = pCharacteristic->getValue();
    M5.Lcd.println(value.c_str());

    String str=value.c_str();
    stmp=str.substring(0,5);
    if(stmp.compareTo("start") ==0) {
      pCharacteristic->setValue("Start Acquisition");
      pCharacteristic->notify(); 
      int a=str.indexOf(',');
      int b=str.lastIndexOf(',');
      stmp=str.substring(a+1,b);
      acq_n_samples=stmp.toInt(); //number of samples
      stmp= str.substring(b+1);
      acq_sample_rate = stmp.toInt(); //sample rate in s
      //M5.Lcd.println(String(aq_time_s));
      //M5.Lcd.println(String(aq_sr));
      acq_flag = true;
      acq_time=millis();
    }

    stmp=str.substring(0,4);
    if(stmp.compareTo("stop") ==0) {
      Serial.println(str);
      Serial.println("in stop");
      acq_flag = false;
      acq_samples_aquired = 0;
      pCharacteristic->setValue("Stoped Acquisition");
      pCharacteristic->notify(); 
    }
  }
};

//setups the necessary hardware
void setup() {
  Serial.begin(115200);
  M5.begin();
  M5.Lcd.setRotation(1);
  M5.Lcd.fillScreen(BLACK);
  M5.Lcd.setCursor(0, 0);
  M5.Lcd.setTextSize(2);
  M5.Lcd.println("AAIB 25/26 (v1)");

  BLEDevice::init(DEVICE_NAME);
  BLEServer *pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());
  BLEService *pService = pServer->createService(SERVICE_UUID);
  pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE |
                                         BLECharacteristic::PROPERTY_NOTIFY |
                                         BLECharacteristic::PROPERTY_INDICATE
                                       );
  pCharacteristic->setCallbacks(new MyCallbacks());
  pCharacteristic->addDescriptor(new BLE2902());

  pService->start();
  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();
  M5.Lcd.println("BLE running.");
  M5.Lcd.print("Name: ");
  M5.Lcd.println(DEVICE_NAME);

  M5.Imu.Init(); 
  M5.Lcd.println("IMU Ready.");
}

//Main Loop
void loop() {
  char buf[60];
 
  if (deviceConnected) {
    //If button B pressed, post BLE message and start/stop continuos aquisition
    if(M5.BtnB.wasPressed()) {
      M5.Lcd.println("Button B pressed!");
      pCharacteristic->setValue("Button B pressed!");
      pCharacteristic->notify();
      acq_flag = !acq_flag;
      if(acq_flag){
        M5.Lcd.println("Aquisition Start");
      }
      else {
        M5.Lcd.println("Aquisition Stop");
      }
      acq_time=millis();
    }

    //If button B pressed, post BLE message and does a single aquisition
    if(M5.BtnA.wasPressed()) {
      M5.Lcd.println("Button A pressed!");
      pCharacteristic->setValue("Button A pressed!");
      pCharacteristic->notify();

      //Read IMU
      M5.IMU.getGyroData(&gyroX, &gyroY, &gyroZ);
      M5.IMU.getAccelData(&accX, &accY, &accZ);
      M5.IMU.getAhrsData(&pitch, &roll, &yaw);
      M5.IMU.getTempData(&temp);

      snprintf(buf, sizeof(buf), "Gyro: %6.2f, %6.2f, %6.2f", gyroX, gyroY, gyroZ);
      M5.Lcd.printf(buf);
      pCharacteristic->setValue(buf);
      pCharacteristic->notify();
      
      snprintf(buf, sizeof(buf), "Acc: %6.2f, %6.2f, %6.2f", accX, accY, accZ);
      M5.Lcd.printf(buf);
      pCharacteristic->setValue(buf);
      pCharacteristic->notify();

      snprintf(buf, sizeof(buf), "PRY: %6.2f, %6.2f, %6.2f", pitch, roll, yaw);
      M5.Lcd.printf(buf);
      pCharacteristic->setValue(buf);
      pCharacteristic->notify();

      snprintf(buf, sizeof(buf), "Temp %.2f", temp);
      M5.Lcd.printf(buf);
      pCharacteristic->setValue(buf);
      pCharacteristic->notify();
    }

    //continuos aquisition 
    if(acq_flag == true && acq_sample_rate > 0) {
      if(millis() - acq_time >= 1000/acq_sample_rate) {
        acq_time=millis();
        M5.IMU.getAccelData(&accX, &accY, &accZ);
        M5.IMU.getGyroData(&gyroX, &gyroY, &gyroZ);
        snprintf(buf, sizeof(buf), "%6.2f, %6.2f, %6.2f, %6.2f, %6.2f, %6.2f", accX, accY, accZ, gyroX, gyroY, gyroZ);
        Serial.println(buf);
        //M5.Lcd.printf(buf);
        pCharacteristic->setValue(buf);
        pCharacteristic->notify(); 
        
        ++acq_samples_aquired;
        if(acq_samples_aquired >= acq_n_samples) {
          acq_flag = false;
          acq_samples_aquired = 0;
          pCharacteristic->setValue("End Acquisition");
          pCharacteristic->notify(); 
        }
      }
    }
  }
  M5.update();
}
