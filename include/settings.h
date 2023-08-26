#define DEBUG_SERIAL    
#define DEBUG_MQTT       
//#define useModulPower   

#define SERIAL_RATE     115200    // Serial speed for status info
#define MAX485_DE       D1        // D0, DE pin on the TTL to RS485 converter
#define MAX485_RE_NEG   D2        // D7, RE pin on the TTL to RS485 converter
#define MAX485_RX       D5        // D5, RO pin on the TTL to RS485 converter
#define MAX485_TX       D6        // D6, DI pin on the TTL to RS485 converter
#define STATUS_LED      D4        // Status LED on the Wemos D1 mini (D4)
#define UPDATE_MODBUS   5         // 1: modbus device is read every second and data are anounced via mqtt
#define UPDATE_STATUS   30        // 10: status mqtt message is sent every 10 seconds
#define WIFICHECK       1         // 1: every second

// Update the below parameters for your project
// Also check NTP.h for some parameters as well
const char mqtt_server[] = "192.168.68.145";    // MQTT server
const int mqtt_server_port = 1883;             // MQTT server port, default is 1883
const char mqtt_user[] = "mqtt";               // MQTT userid
const char mqtt_password[] = "mqtt";        // MQTT password
const char clientID[] = "growatt-zolder";       // MQTT client ID
const char topicRootStart[] = "growatt";      // MQTT root topic for the device, + client ID

// Comment the entire second below for dynamic IP (including the define)
// #define FIXEDIP   1
// IPAddress local_IP(192, 168, 1, 205);     // Set your Static IP address
// IPAddress gateway(192, 168, 1, 254);          // Set your Gateway IP address
// IPAddress subnet(255, 255, 255, 0);
// IPAddress primaryDNS(192, 168, 1, 254);   //optional
// IPAddress secondaryDNS(8, 8, 4, 4); //optional
