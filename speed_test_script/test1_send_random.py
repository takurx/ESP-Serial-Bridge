import serial, os

# COMポートを指定（例: COM3）
ser = serial.Serial("COM17", 115200)
# ser = serial.Serial("COM18", 115200)

while True:
    ser.write(os.urandom(1024))

