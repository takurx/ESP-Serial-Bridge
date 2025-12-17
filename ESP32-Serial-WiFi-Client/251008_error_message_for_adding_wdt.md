# 251008_error_message_for_adding_wdt.md

## cycle 1
```
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino: In function 'void setup()':
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:80:23: error: too many arguments to function 'hw_timer_t* timerBegin(uint32_t)'
   80 |     timer = timerBegin(0, 80, true);                  //timer 0, div 80
      |             ~~~~~~~~~~^~~~~~~~~~~~~
In file included from C:\Users\YoshihiroNakagawa\AppData\Local\Arduino15\packages\esp32\hardware\esp32\3.3.0\cores\esp32/esp32-hal.h:98,
                 from C:\Users\YoshihiroNakagawa\AppData\Local\Arduino15\packages\esp32\hardware\esp32\3.3.0\cores\esp32/Arduino.h:44,
                 from C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:12:
C:\Users\YoshihiroNakagawa\AppData\Local\Arduino15\packages\esp32\hardware\esp32\3.3.0\cores\esp32/esp32-hal-timer.h:35:13: note: declared here
   35 | hw_timer_t *timerBegin(uint32_t frequency);
      |             ^~~~~~~~~~
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:81:25: error: too many arguments to function 'void timerAttachInterrupt(hw_timer_t*, void (*)())'
   81 |     timerAttachInterrupt(timer, &resetModule, true);  //attach callback
      |     ~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\YoshihiroNakagawa\AppData\Local\Arduino15\packages\esp32\hardware\esp32\3.3.0\cores\esp32/esp32-hal-timer.h:50:6: note: declared here
   50 | void timerAttachInterrupt(hw_timer_t *timer, void (*userFunc)(void));
      |      ^~~~~~~~~~~~~~~~~~~~
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:82:5: error: 'timerAlarmWrite' was not declared in this scope; did you mean 'timerWrite'?
   82 |     timerAlarmWrite(timer, TIMEOUT * 1000, false);    //set time in us
      |     ^~~~~~~~~~~~~~~
      |     timerWrite
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:83:5: error: 'timerAlarmEnable' was not declared in this scope; did you mean 'timerAlarm'?
   83 |     timerAlarmEnable(timer);                          //enable interrupt
      |     ^~~~~~~~~~~~~~~~
      |     timerAlarm
exit status 1

Compilation error: too many arguments to function 'hw_timer_t* timerBegin(uint32_t)'
```

## cycle 2
```
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:34:1: error: expected ',' or ';' before 'hw_timer_t'
   34 | hw_timer_t *timer = NULL;
      | ^~~~~~~~~~
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino: In function 'void setup()':
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:80:5: error: 'timer' was not declared in this scope; did you mean 'time'?
   80 |     timer = timerBegin(1000000);                       //timer 1MHz
      |     ^~~~~
      |     time
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino: In function 'void loop()':
C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\ESP32-Serial-WiFi-Client\ESP32-Serial-WiFi-Client.ino:150:16: error: 'timer' was not declared in this scope; did you mean 'time'?
  150 |     timerWrite(timer, 0); //reset timer (feed watchdog)
      |                ^~~~~
      |                time
exit status 1

Compilation error: expected ',' or ';' before 'hw_timer_t'
```