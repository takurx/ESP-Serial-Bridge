# 260612_speed_test_result-7.md

## test1, host x3 -> client x3, ほぼ110000 bps
- com11 -> com8
```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge> cd .\speed_test_script\
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_send_random_com11.py         
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_send_random_com11.py", line 12, in <module>
    ser.write(os.urandom(1024))
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 321, in write
    win32.GetOverlappedResult(self._port_handle, self._overlapped_write, ctypes.byref(n), True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script>
```

```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge> cd .\speed_test_script\
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com8.py        
78904.37 bps
118948.96 bps
118935.09 bps
108012.09 bps
118890.13 bps
109074.76 bps
118993.17 bps
118980.43 bps
108985.46 bps
119026.42 bps
118868.41 bps
109074.15 bps
118933.56 bps
109093.45 bps
118957.71 bps
118971.28 bps
109073.04 bps
118921.73 bps
118952.31 bps
109042.43 bps
118919.40 bps
109062.70 bps
118947.09 bps
118953.07 bps
109057.76 bps
118981.41 bps
118940.09 bps
109033.70 bps
118941.63 bps
109083.19 bps
118934.55 bps
118943.19 bps
109058.79 bps
118939.84 bps
118973.59 bps
107710.14 bps
118934.79 bps
109054.84 bps
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_receive_random_com8.py", line 14, in <module>
    data = ser.read(1024)
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
        self._port_handle,
        ctypes.byref(self._overlapped_read),
        ctypes.byref(rc),
        True)
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

- com12 -> com9
```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge> cd .\speed_test_script\
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_send_random_com12.py      
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_send_random_com12.py", line 12, in <module>
    ser.write(os.urandom(1024))
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 321, in write
    win32.GetOverlappedResult(self._port_handle, self._overlapped_write, ctypes.byref(n), True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge> cd .\speed_test_script\
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com9.py 
79276.25 bps
118922.99 bps
117907.55 bps
109042.28 bps
118940.42 bps
109035.89 bps
118983.94 bps
118923.49 bps
109093.57 bps
118917.09 bps
118935.20 bps
109072.29 bps
118956.84 bps
109047.62 bps
118960.95 bps
118921.89 bps
109094.30 bps
118927.85 bps
118955.90 bps
109043.92 bps
118968.01 bps
109120.15 bps
118949.45 bps
118958.04 bps
109044.50 bps
118944.34 bps
118955.08 bps
109043.92 bps
118925.41 bps
109046.26 bps
118943.05 bps
118919.54 bps
109048.17 bps
118961.53 bps
118915.12 bps
109058.57 bps
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_receive_random_com9.py", line 14, in <module>
    data = ser.read(1024)
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
        self._port_handle,
        ctypes.byref(self._overlapped_read),
        ctypes.byref(rc),
        True)
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

- com13 -> com14
```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge> cd .\speed_test_script\
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_send_random_com13.py   
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_send_random_com13.py", line 12, in <module>
    ser.write(os.urandom(1024))
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 321, in write
    win32.GetOverlappedResult(self._port_handle, self._overlapped_write, ctypes.byref(n), True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge> cd .\speed_test_script\
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com14.py
79261.24 bps
118221.66 bps
118915.23 bps
109017.20 bps
118945.11 bps
109115.64 bps
118983.42 bps
118951.45 bps
109017.95 bps
118957.06 bps
118947.04 bps
109032.09 bps
118960.98 bps
109067.58 bps
118924.91 bps
118910.89 bps
109045.88 bps
118959.11 bps
118996.94 bps
109061.29 bps
118959.17 bps
109013.42 bps
118957.99 bps
119040.42 bps
109090.22 bps
118948.74 bps
118862.33 bps
109128.65 bps
118914.57 bps
109059.20 bps
118945.14 bps
118914.40 bps
109069.54 bps
112813.63 bps
118958.54 bps
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_receive_random_com14.py", line 14, in <module>
    data = ser.read(1024)
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
        self._port_handle,
        ctypes.byref(self._overlapped_read),
        ctypes.byref(rc),
        True)
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

## test2, host x3 <- client x3、ほぼ115200 bps
- com11 <- com8
```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com11.py   
115474.55 bps
115230.73 bps
115233.72 bps
115200.21 bps
115255.50 bps
115236.84 bps
115246.14 bps
115226.77 bps
115204.10 bps
115229.06 bps
115240.27 bps
115193.29 bps
115251.45 bps
115220.17 bps
115250.19 bps
115220.74 bps
115210.54 bps
115234.13 bps
115235.09 bps
115225.79 bps
115237.10 bps
115212.96 bps
115213.53 bps
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_receive_random_com11.py", line 14, in <module>
    data = ser.read(1024)
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
        self._port_handle,
        ctypes.byref(self._overlapped_read),
        ctypes.byref(rc),
        True)
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_send_random_com8.py    
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_send_random_com8.py", line 12, in <module>
    ser.write(os.urandom(1024))
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 321, in write
    win32.GetOverlappedResult(self._port_handle, self._overlapped_write, ctypes.byref(n), True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

- com12 <- com9
```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com12.py
115411.69 bps
115224.60 bps
115257.53 bps
115234.93 bps
115218.16 bps
115222.64 bps
115214.22 bps
115231.25 bps
115216.75 bps
115241.97 bps
115234.88 bps
115230.91 bps
115236.35 bps
115229.60 bps
115224.29 bps
115210.38 bps
115248.00 bps
115235.45 bps
115241.14 bps
115210.90 bps
115238.80 bps
115228.90 bps
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_receive_random_com12.py", line 14, in <module>
    data = ser.read(1024)
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
        self._port_handle,
        ctypes.byref(self._overlapped_read),
        ctypes.byref(rc),
        True)
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_send_random_com9.py       
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_send_random_com9.py", line 12, in <module>
    ser.write(os.urandom(1024))
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 321, in write
    win32.GetOverlappedResult(self._port_handle, self._overlapped_write, ctypes.byref(n), True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

- com13 <- com14
```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com13.py   
115338.03 bps
115252.66 bps
115220.97 bps
115215.46 bps
115238.10 bps
115212.26 bps
115225.17 bps
115246.17 bps
115200.75 bps
115221.95 bps
115242.35 bps
115218.09 bps
115234.52 bps
115198.51 bps
115234.83 bps
115239.26 bps
115217.88 bps
115226.69 bps
115217.13 bps
115237.95 bps
115214.66 bps
115218.09 bps
115229.70 bps
115233.16 bps
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_receive_random_com13.py", line 14, in <module>
    data = ser.read(1024)
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
        self._port_handle,
        ctypes.byref(self._overlapped_read),
        ctypes.byref(rc),
        True)
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```

```
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_send_random_com14.py      
Traceback (most recent call last):
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script\test1_send_random_com14.py", line 12, in <module>
    ser.write(os.urandom(1024))
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\.venv\Lib\site-packages\serial\serialwin32.py", line 321, in write
    win32.GetOverlappedResult(self._port_handle, self._overlapped_write, ctypes.byref(n), True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> 
```


