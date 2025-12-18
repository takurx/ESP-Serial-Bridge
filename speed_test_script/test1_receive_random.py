import serial, time

# com8, client
# com7, host
ser = serial.Serial("COM8", 115200)
# ser = serial.Serial("COM7", 115200)

count = 0
start = time.time()

while True:
    data = ser.read(1024)
    count += len(data)
    elapsed = time.time() - start
    if elapsed >= 1.0:
        # kbps = (count / elapsed) / 1024.0   # KB/s
        byte_per_sec = (count / elapsed)
        kbps = byte_per_sec/ 1024.0   # KB/s
        data_bps = byte_per_sec * 8          # データ部のみ（8bit換算）
        total_bps = byte_per_sec * 10        # UART全体（8N1の場合）
        # print(f"{kbps:.2f} KB/s")
        # print(f"{data_bps:.2f} bps")
        print(f"{total_bps:.2f} bps")
        count = 0
        start = time.time()

