import serial, time

ser = serial.Serial("COM18", 115200)
# ser = serial.Serial("COM17", 115200)

count = 0
start = time.time()

while True:
    data = ser.read(1024)
    count += len(data)
    elapsed = time.time() - start
    if elapsed >= 1.0:
        #print(f"{count/elapsed/1024:.2f} KB/s")
        print(f"{count*8/elapsed:.2f} bps")
        count = 0
        start = time.time()

