import serial, os

# COMポートを指定（例: COM3）
ser = serial.Serial("COM29", 115200)
# ser = serial.Serial("COM6", 115200)
# ser = serial.Serial("COM11", 115200)
# ser = serial.Serial("COM24", 115200)
# ser = serial.Serial("COM25", 115200)
# ser = serial.Serial("COM26", 115200)

while True:
    ser.write(os.urandom(1024))

