#pragma once

// WiFi
static const char* WIFI_SSID = "ssid_esp_uart_bridge3x3";
static const char* WIFI_PASS = "password_esp_uart_bridgeAAAA";
static const uint32_t WIFI_CONNECT_TIMEOUT_MS = 15000;

// Bridge server
// ESP-Serial-Bridge のIP（APモードなら 192.168.4.1 のことが多い）
static const char* BRIDGE_HOST = "192.168.4.1";

// UARTごとのTCPポート（ESP-Serial-Bridge側設定に合わせる）
static const uint16_t BRIDGE_PORTS[3] = {
  8880, // COM0
  8881, // COM1
  8882  // COM2
};

// UART pins/baud (README pinningに合わせた初期値) :contentReference[oaicite:2]{index=2}
static const int UART0_RX_PIN = 21;
static const int UART0_TX_PIN = 1;
static const uint32_t UART0_BAUD = 115200;
static const bool UART0_INVERT = false;

static const int UART1_RX_PIN = 26;
static const int UART1_TX_PIN = 25;
static const uint32_t UART1_BAUD = 115200;
static const bool UART1_INVERT = false;

static const int UART2_RX_PIN = 15;
static const int UART2_TX_PIN = 4;
static const uint32_t UART2_BAUD = 115200;
static const bool UART2_INVERT = false;

// TCP tuning
static const bool TCP_NODELAY = true;
static const int CLIENT_KEEPALIVE_SEC = 15;
static const uint32_t RECONNECT_INTERVAL_MS = 500;

// Chunk sizes
static const size_t TX_CHUNK = 256;
static const size_t RX_CHUNK = 256;

// Logging
// UART0を外部機器に使うならログはOFF推奨（USB-Serialと競合するため）
#define ENABLE_USB_LOG 0
