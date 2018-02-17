#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>


#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
ESP8266WebServer server(80);

const char* ssid = "Telstra00F027";
const char* password =  "yrtqbgr9fann";
float h = 0;
float t = 0;
int output = 0;
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  //Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);  //Connect to the WiFi network

  while (WiFi.status() != WL_CONNECTED) {  //Wait for connection

    delay(500);
    //Serial.println("Waiting to connect...");

  }

  //Serial.print("IP address: ");
  //Serial.println(WiFi.localIP());  //Print the local IP

  server.on("/json", handleJSON); //Associate the handler function to the path
  server.on("/led", handleLED); //Associate the handler function to the path
  server.begin(); //Start the server
  //Serial.println("Server listening");

}

void loop() {

  server.handleClient(); //Handling of incoming requests
  //Serial.println(millis());
  //delay(500);
  //h = dht.readHumidity();
  //t = dht.readTemperature();
}
void handleLED() {
  String message;
  if (output == 0) {
    //Serial.println("LOW");
    output = 1;

    message += "[{\"LED\":";
    message += "ON";
    message += "}]";
    server.send(200, "text/plain", message);
    digitalWrite(LED_BUILTIN, LOW);
    return;
  } else {
    //Serial.println("HIGH");
    output = 0;
    message += "[{\"LED\":";
    message += "OFF";
    message += "}]";
    server.send(200, "text/plain", message);
    digitalWrite(LED_BUILTIN, HIGH);
    return;
  }

}
void handleJSON() { //Handler for the JSON path

  if (server.hasArg("plain") == false) { //Check if body received
    String message;
    //message += "HTTP/1.1 200 OK\r\n";
    //message += "Content-Type: application/json;charset=utf-8\r\n";
    //message += "Server: Arduino\r\n";
    //message += "Connection: close\r\n";

    message += "[{\"temp\":";
    message += t;
    message += ", \"humid\":";
    message += h;
    message += "}]";
    server.send(200, "text/plain", message);
    //Serial.println(message);
    //server.send(200, "text/plain", "Body not received");
    return;

  }
}
