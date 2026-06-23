# ESP32-Serial-Bridge, ESP32S3-Serial-Bridge, 3 port concurrent

---

# Takurx's Notes

## Project Overview

This repository is a fork of [AlphaLima/ESP32-Serial-Bridge](https://github.com/AlphaLima/ESP32-Serial-Bridge) (via [Yuri's fork](https://github.com/yuri-rage/ESP32-Serial-Bridge)).  
It provides a transparent WiFi (TCP/UDP) ↔ multi-UART bridge, targeting both ESP32 and **ESP32-S3** boards.

In addition to the original/Yuri functionality, this fork adds:

- ESP32-S3 (PlatformIO) support for Bridge (Host) and Client
- 3-UART concurrent client (`Kerberos`)
- Hardware flow control (CTS/RTS) pin definitions
- Buffer size tuning for high-throughput stability
- Non-blocking TX with pending queue
- PCB design (KiCad) for ESP32 and ESP32-S3
- 3D-printable enclosure STL files
- Speed test scripts and result logs

---

## Repository Structure

```
ESP-Serial-Bridge/
├── ESP-Serial-Bridge/                        # Original Arduino IDE sketch (ESP32/ESP8266)
│   ├── ESP-Serial-Bridge.ino
│   └── config.h
│
├── ESP32-Serial-WiFi-Client/                 # Arduino IDE single-UART TCP/UDP Client (Yuri)
│   ├── ESP32-Serial-WiFi-Client.ino
│   └── client_config.h
│
├── ESP32-Serial-WiFi-Client-Kerberos/        # Arduino IDE 3-UART concurrent Client (ESP32)
│   ├── ESP32-Serial-WiFi-Client-Kerberos.ino
│   └── client_config.h
│
├── pio-ESP32S3-Serial-WiFi-Bridge/           # PlatformIO Bridge (Host) for ESP32-S3
│   ├── src/main.cpp
│   ├── include/config.h
│   └── platformio.ini
│
├── pio-ESP32S3-Serial-WiFi-Client-Kerberos/  # PlatformIO 3-UART Client (Kerberos) for ESP32-S3
│   ├── src/main.cpp
│   ├── include/client_config.h
│   └── platformio.ini
│
├── pcb_kicad/
│   ├── esp_serial_bridge_pcb/                # KiCad PCB for ESP32
│   └── esp32s3_serial_bridge_pcb/            # KiCad PCB for ESP32-S3 (Kerberos)
│
├── case_3dprint/                             # 3D-printable enclosure STL files
├── speed_test_script/                        # Python speed-test scripts and result logs
└── README.md
```

---

## Recent Updates (Takurx)

### English

#### **Near Full-Speed 3-Port Operation Achieved (Jun 2026)**
Applied buffer optimizations (developed for the Bridge/Host) to the Client (Kerberos) side.  
Result: all three UARTs now operate at **≈ 110,000–115,200 bps** in both directions simultaneously.

- Host → Client (×3 ports): ≈ **110,000 bps** (previously ≈ 13,000 bps)
- Client → Host (×3 ports): ≈ **115,200 bps** (stable)

Key changes:
- `setRxBufferSize(4096)` / `setTxBufferSize(4096)` applied to all UART ports before `begin()`
- Non-blocking TX: `availableForWrite()` used to avoid blocking `write()` calls
- Overflow data stored in a per-channel `txPendingBuf[]` queue and flushed next loop
- Bulk TCP read using `readBytes()` instead of byte-by-byte loop

#### **Buffer Separation: SOFTWAREBUFFERSIZE / HARDWAREBUFFERSIZE (Jun 2026)**
Separated buffer constant into two named constants in `config.h` for clarity:

| Constant | Size | Role |
|---|---|---|
| `HARDWAREBUFFERSIZE` | 4096 B | HardwareSerial internal ring buffer (ISR ← UART FIFO) |
| `SOFTWAREBUFFERSIZE` | 1024 B | Application working buffer (`buf1`, `buf2`, `txPending`) |

Data flow:
```
[UART RX] UART HW FIFO (1024B) → HardwareSerial ring buffer (4096B) → buf2[1024B] → TCP TX
[TCP RX]  TCP RX buffer (lwIP) → buf1[1024B] → HardwareSerial TX ring buffer (4096B) → UART TX
```

#### **pio-ESP32S3-Serial-WiFi-Client-Kerberos — 3-UART PlatformIO Client (Apr 2026)**
Added a PlatformIO version of the 3-UART concurrent client for ESP32-S3.  
Mirrors the same buffer/non-blocking approach as the Bridge Host side.

#### **PCB Design (KiCad) (Mar 2026)**
Added KiCad PCB designs (schematic + layout + Gerber) for:
- `esp_serial_bridge_pcb` — for ESP32 modules
- `esp32s3_serial_bridge_pcb` — for ESP32-S3 modules (Kerberos)

#### **pio-ESP32S3-Serial-WiFi-Bridge — ESP32-S3 PlatformIO Port (Feb 2026)**
New PlatformIO project targeting **RYMCU ESP32-S3-DevKitC-1** (board: `rymcu-esp32-s3-devkitc-1`).

Notable changes from original:
- All 3 UART ports configured with CTS/RTS pins (flow control disabled by default, can be enabled)
- `HARDWAREBUFFERSIZE` = 4096 bytes applied via `setRxBufferSize()` / `setTxBufferSize()`
- Non-blocking TX pending queue (`txPending[]`, `txPendingLen[]`) per UART port
- Bulk TCP read with `readBytes()` instead of 1-byte-at-a-time loop
- Hostname changed to `ESP32-S3`

#### **3-UART Concurrent Client — "Kerberos" (Feb 2026)**
Added `ESP32-Serial-WiFi-Client-Kerberos` (Arduino IDE) and its PlatformIO equivalent.  
Establishes three simultaneous TCP connections (one per UART) to the Bridge Host.

#### **Speed Test Results Summary**

| Date | Config | Host → Client | Client → Host |
|---|---|---|---|
| Dec 2025 | ESP32 AP mode, 1 port, flow ctrl None | ≈ 13,000 bps (drops to 7,000) | ≈ 100,000 bps (stable) |
| Feb 2026 | ESP32-S3 ↔ ESP32-S3, 1 port, flow ctrl ON | avg ≈ 82,000 bps | avg ≈ 20,000 bps |
| Feb 2026 | ESP32-S3 ↔ ESP32-S3, 1 port, flow ctrl OFF | avg ≈ 50,000 bps | avg ≈ 20,000 bps |
| Feb 2026 | ESP32-S3 ↔ ESP32-S3, 3 ports, flow ctrl None | 600–45,000 bps | 7,000–13,000 bps |
| Feb 2026 | 3 ports, flow ctrl ON/OFF | ≈ 13,000 bps avg | ≈ 10,000 bps avg |
| **Jun 2026** | **3 ports, buffer opt. applied to client**, flow ctrl None | **≈ 110,000 bps** | **≈ 115,200 bps** |

#### **Watch Dog Timer Bug Fix (Dec 2025)**
Fixed a critical bug where the system would enter an infinite loop when the Host side crashed and the Watch Dog Timer failed to activate. Now properly handles three scenarios:
1. Client-side crash (Client Reset) → Recovers with input from Host side
2. Host-side crash with quick recovery (Host Reset) → System continues normally
3. Host-side crash without recovery (Host OFF) → Client automatically resets every 30 seconds via Watch Dog Timer

#### **3D-Printable Case (Dec 2025)**
Added STL files for 3D-printable enclosure (box and cover, including v2 versions).

---

### 日本語

#### **3ポート同時フルスピード動作を達成 (2026年6月)**
Bridge（Host）側で開発したバッファ最適化手法をClient（Kerberos）側にも適用。  
全3ポートで**約110,000〜115,200 bps**の双方向同時通信が可能になった。

- Host → Client（×3ポート）: 約 **110,000 bps**（以前は約13,000 bps）
- Client → Host（×3ポート）: 約 **115,200 bps**（安定）

主な変更点：
- `setRxBufferSize(4096)` / `setTxBufferSize(4096)` を全UARTポートの `begin()` 前に適用
- 非ブロッキングTX: `availableForWrite()` でブロッキング `write()` を回避
- 書けなかったデータをポートごとの `txPendingBuf[]` キューに退避し次ループで再送
- TCPの一括読み出し（`readBytes()`）で1バイトずつのループを排除

#### **バッファ定数の分離: SOFTWAREBUFFERSIZE / HARDWAREBUFFERSIZE (2026年6月)**
`config.h` のバッファ定数を2つに分離して明確化：

| 定数 | サイズ | 役割 |
|---|---|---|
| `HARDWAREBUFFERSIZE` | 4096 B | HardwareSerial内部リングバッファ（ISR ← UART FIFO） |
| `SOFTWAREBUFFERSIZE` | 1024 B | アプリ作業バッファ（`buf1`, `buf2`, `txPending`） |

#### **pio-ESP32S3-Serial-WiFi-Client-Kerberos — 3UART PlatformIOクライアント (2026年4月)**
ESP32-S3向け3UART同時クライアントのPlatformIO版を追加。  
BridgeHost側と同じバッファ/非ブロッキング手法を適用。

#### **PCB設計（KiCad）(2026年3月)**
以下のKiCad PCB設計（回路図 + レイアウト + Gerber）を追加：
- `esp_serial_bridge_pcb` — ESP32モジュール用
- `esp32s3_serial_bridge_pcb` — ESP32-S3モジュール（Kerberos）用

#### **pio-ESP32S3-Serial-WiFi-Bridge — ESP32-S3 PlatformIO移植 (2026年2月)**
ESP32-S3（RYMCU ESP32-S3-DevKitC-1）向けの新しいPlatformIOプロジェクト。

主な変更点：
- 全3 UARTポートにCTS/RTSピンを定義（デフォルトはフロー制御無効）
- `HARDWAREBUFFERSIZE` = 4096バイトをRX/TXバッファ両方に適用
- ポートごとの非ブロッキング送信保留キュー（`txPending[]`）を実装
- TCP一括読み出しに変更（`readBytes()` 使用）
- ホスト名を `ESP32-S3` に変更

#### **3UART同時クライアント「Kerberos」(2026年2月)**
3つのTCP接続を同時確立するクライアント `ESP32-Serial-WiFi-Client-Kerberos`（Arduino IDE版）とそのPlatformIO版を追加。

#### **速度テスト結果サマリ**

| 日付 | 構成 | Host → Client | Client → Host |
|---|---|---|---|
| 2025年12月 | ESP32 APモード、1ポート、フロー制御なし | 約13,000 bps（時々7,000に低下） | 約100,000 bps（安定） |
| 2026年2月 | ESP32-S3同士、1ポート、フロー制御あり | 平均 約82,000 bps | 平均 約20,000 bps |
| 2026年2月 | ESP32-S3同士、1ポート、フロー制御なし | 平均 約50,000 bps | 平均 約20,000 bps |
| 2026年2月 | ESP32-S3同士、3ポート同時、フロー制御なし | 600〜45,000 bps | 7,000〜13,000 bps |
| 2026年2月 | 3ポート、フロー制御あり/なし | 平均 約13,000 bps | 平均 約10,000 bps |
| **2026年6月** | **3ポート、クライアント側バッファ最適化適用後**、フロー制御なし | **約110,000 bps** | **約115,200 bps** |

#### **Watch Dog Timer バグ修正 (2025年12月)**
Host側が落ちた時に無限ループに陥り、Watch Dog Timerが効かなかった重大なバグを修正。以下の3つのケースに対応:
1. Client側が落ちた場合（ClientのReset）→ Host側からの入力で回復
2. Host側が落ちてすぐ回復した場合（HostのReset）→ 正常動作
3. Host側が落ちて回復しない場合（HostのOFF）→ 30秒ごとにWatch Dog TimerでClientを自動Reset

#### **3Dプリント用ケース (2025年12月)**
3Dプリント可能なケースのSTLファイルを追加（ボックスとカバー、v2バージョンを含む）。

---

## Hardware: ESP32-S3 Pin Assignment

### Bridge Host (`pio-ESP32S3-Serial-WiFi-Bridge`)

| Port | RX Pin | TX Pin | CTS Pin | RTS Pin | TCP Port | UDP Port |
|---|---|---|---|---|---|---|
| COM0 | GPIO1 | GPIO43 | GPIO16 | GPIO15 | 8880 | 14550 |
| COM1 | GPIO18 | GPIO17 | GPIO10 | GPIO9  | 8881 | 14551 |
| COM2 | GPIO38 | GPIO37 | GPIO36 | GPIO35 | 8882 | 14552 |

- Static IP (AP mode): `192.168.4.1`
- Default SSID: `ssid_esp_uart_bridge3x3`
- Hardware flow control: pins defined, **disabled by default** (comment in code to enable)

---

# Yuri's Notes

This fork is compatible with both the ESP32 and ESP8266.

Because the ESP8266 has some idiosyncrasies with its hardware serial ports, I used SoftwareSerial to implement the ESP8266 bridge.  It is limited to ~115200 baud and will likely prove less reliable than an ESP32. `BLUETOOTH` (hardware limitation) and `PROTOCOL_UDP` (software limitation) are not available on the ESP8266.

As is, the sketch will compile, build, and upload without errors for the ESP32.  Edit `config.h` to configure and build for ESP8266.

There are many configurable parameters in `config.h`. Edit to suit your needs - inline comments should provide clarity.

## Major update, Apr 2023:
* Fixed compatibility with Arduino framework 2.0
* Added compatibility with PlatformIO.
* Implemented `PROTOCOL_UDP` (UDP broadcast)
* `PROTOCOL_TCP` and `PROTOCOL_UDP` can be used simultaneously, though doing so may result in serial traffic conflicts if your client connections are not managed carefully.
* Added `ESP32-Serial-WiFi-Client.ino` in a separate sketch folder to make an ESP32 TCP or UDP client that connects to the ESP-Serial-Bridge. Edit `client_config.h` and upload to a second board.
* Multiple bugs (possible buffer overruns) are fixed in the latest commit(s).
* Latest commits also include some styling/readability edits, though I can easily admit that it isn't the "prettiest" of C++ projects.

---

# ESP32-Serial-Bridge (Original by AlphaLima)

Transparent WiFi (TCP) to all three UART Bridge, supports both AP and STATION WiFi modes. The .ino file is the code for the ESP32. Use Arduino IDE for ESP32 to compile and upload it to the ESP32.
I made this project in order to connect Flight equipment devices devices like (Radio, Vario FLARM), to a Flight Computer (Kobo, Smartphones etc.),  but it is not limited to that. You can use it wherever you want, but on your own risk. Read license file for more details.                                  

===============================================================

Used Libraries: (must be installed in the arduino IDE):

https://github.com/espressif/arduino-esp32


===============================================================

In some cases the memorylayout is to small for this scetch.
If you face this problem you can either disable Bluetooth by removing
#define BLUETOOTH
in config.h 
or change the partition size as described here:
https://desire.giesecke.tk/index.php/2018/04/20/change-partition-size-arduino-ide/

Arduino hardware configuration:

https://github.com/AlphaLima/ESP32-Serial-Bridge/blob/master/Settings.jpg

===============================================================

example usecases:

https://www.youtube.com/watch?v=K2Hia06IMtk

https://www.youtube.com/watch?v=GoSxlQvuAhg

# Hardware (Original ESP32)
here is the wiring diagram recomendation:
https://raw.githubusercontent.com/AlphaLima/ESP32-Serial-Bridge/master/ESP32-SerialBridge.jpg             
Pinning                                                                                     
COM0 Rx <-> GPIO21                                                                               
COM0 Tx <-> GPIO01                                                                                 
COM1 Rx <-> GPIO16                                                                               
COM1 Tx <-> GPIO17                                                                              
COM2 Rx <-> GPIO15                                                                               
COM2 Tx <-> GPIO04                                                                              

NOTE: The PIN assignment has changed and may not look straigt forward (other PINs are marke as Rx/Tx), but this assignment allows to flash via USB also with hooked MAX3232 serial drivers.

I recomend to start your project with a Node32s or compatible evaluation board. For a TTL to RS232 level conversion search google for "TTL RS3232 Converter"



https://tech.scargill.net/wp-content/uploads/2017/05/ESP326.jpg
