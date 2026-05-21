#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>  // ← 1. ДОБАВИЛИ ЭТО

// 📶 Настройки
const char* ssid = "Galaxy A34 5G B536";
const char* password = "Shalalala";
const IPAddress serverIP(10, 108, 205, 202); 
const uint16_t serverPort = 5000; 
const int buttonPin = 25;        

WiFiUDP udpClient; // Объявили клиент

void setup() {
  Serial.begin(9600); // Увеличил скорость для удобства отладки
  pinMode(buttonPin, INPUT_PULLUP); 

  Serial.print("Подключение к Wi-Fi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ Wi-Fi подключён! IP: " + WiFi.localIP().toString());
  udpClient.begin(0); 
  Serial.println("📡 UDP клиент готов.");
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    sendJsonPacket();
    delay(200); // Защита от простого спама
  }
}

void sendJsonPacket() {
  StaticJsonDocument<256> doc;
  
  // Заполняем данные
  doc["tanks"] = "tanks";
  doc["record in tanks"] = millis();
  doc["races"] = "races";
  doc["record in races"] = millis();

  String payload;
  serializeJson(doc, payload);

  // 2. ИСПРАВИЛИ: используем udpClient вместо udp
  udpClient.beginPacket(serverIP, serverPort);
  udpClient.print(payload); 
  int status = udpClient.endPacket();

  // Лог для отладки (полезно видеть, что ушло)
  if (status) {
    Serial.println("✅ Отправлено: " + payload);
  } else {
    Serial.println("❌ Ошибка отправки");
  }
}