/*********************************************************************************
 * client_config.h
 * 
 * Added ESP32-Serial-WiFi-Client   -- Yuri - Apr 2023
 * 
*********************************************************************************/
#ifndef CLIENT_CONFIG_H
#define CLIENT_CONFIG_H

#include <WiFi.h>

#define DEBUG              // comment to suppress system serial messages

#define OTA_HANDLER        // uncomment to enable OTA programming

#define SSID   "ssid_esp_uart_bridge3x3"      // SSID to join
#define PASSWD "password_esp_uart_bridgeAAAA"  // wiFi password

#define BUFFERSIZE 1024

#define VERSION "2.0-ESP32"

#define PROTOCOL_TCP                       // PROTOCOL_TCP or PROTOCOL_UDP
//#define PROTOCOL_UDP                       // PROTOCOL_TCP or PROTOCOL_UDP
#define HOST_IP IPAddress(192, 168, 4, 1)  // only used for PROTOCOL_TCP
//#define HOST_PORT 14550                    // UDP port
#define CLIENT_BAUD 115200
#define CLIENT_PARAM SERIAL_8N1

// COM0, OK
#define HOST_PORT 8880                    // TCP port
#define CLIENT_TXPIN 1
#define CLIENT_RXPIN 21

// COM1, Fail ESP32-DevKitC-VE ESP32-WROVER-E 8MB
// ESP32-WROVER-E connected PSRAM and it use GPIO17, 16
// So it is Non-Connect
// #define HOST_PORT 8881                    // TCP port
// #define CLIENT_TXPIN 25
// #define CLIENT_RXPIN 26

// May work ESP32-DevKitC-32E ESP32-WROOM-32E 4MB
// #define HOST_PORT 8881                    // TCP port
// #define CLIENT_TXPIN 17
// #define CLIENT_RXPIN 16

// COM2, OK
// #define HOST_PORT 8882                    // TCP port
// #define CLIENT_TXPIN 4
// #define CLIENT_RXPIN 15

/**************************  DO NOT EDIT BELOW HERE **************************/
// perhaps a clever way to include/exclude serial debug messages...
#ifdef DEBUG
    #define debug Serial
#else
    class Debug: public Print {
        virtual size_t write(byte b) { return 0; }
    };
    Debug debug;
#endif

#endif  // CLIENT_CONFIG_H
