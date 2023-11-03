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
#define DEVICE_NAME         "m5-stack"
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


//Callback on connection
class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      M5.Lcd.println("BLE connect");
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      M5.Lcd.println("BLE disconnect");
      deviceConnected = false;
    }
};

//Callback to read and write messages
class MyCallbacks: public BLECharacteristicCallbacks {
  void onRead(BLECharacteristic *pCharacteristic) {
    M5.Lcd.println("Tx to RPI");
    pCharacteristic->setValue("Message from M5Stick");
  }
  
  void onWrite(BLECharacteristic *pCharacteristic) {
    M5.Lcd.println("Rx from RPI");
    std::string value = pCharacteristic->getValue();
    M5.Lcd.println(value.c_str());
  }
};

//setups the necessary hardware
void setup() {
  Serial.begin(115200);
  M5.begin();
  M5.Lcd.println("BLE start.");

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

  M5.Lcd.println("IMU Starting");
  M5.Imu.Init(); 
  M5.Lcd.println("IMU Ready.");
}

//Main Loop
void loop() {
  char buf[40];
  
      
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

    //continuos aquisition at 10 samples a second
    if(acq_flag == true) {
      if(millis() - acq_time >= 100) {
        M5.IMU.getAccelData(&accX, &accY, &accZ);
        snprintf(buf, sizeof(buf), "t: %d; Acc: %6.2f, %6.2f, %6.2f", millis()-acq_time, accX, accY, accZ);
        //M5.Lcd.printf(buf);
        pCharacteristic->setValue(buf);
        pCharacteristic->notify(); 
        acq_time=millis();
      }
    }
  }
  M5.update();
}
