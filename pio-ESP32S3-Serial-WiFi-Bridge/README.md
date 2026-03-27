# pio-ESP32S3-Serial-WiFi-Bridge

## memo randomly

- data flow
UART HW FIFO (1024B) → HardwareSerial リングバッファ (4096B) → buf2[1024B] → TCP送信

- buffer description
サイズ	役割
setRxBufferSize(HARDWAREBUFFERSIZE)	4096 bytes	HardwareSerial 内部リングバッファ — ISR が UART FIFO からここへコピーする。loop() が来るまでデータを溜める場所
buf2[NUM_COM][SOFTWAREBUFFERSIZE]	1024 bytes	loop() 内の一時作業バッファ — リングバッファから読み出してTCPへ書くための中継
buf1[NUM_COM][SOFTWAREBUFFERSIZE]	1024 bytes	TCP から読んでシリアルへ書くための中継

