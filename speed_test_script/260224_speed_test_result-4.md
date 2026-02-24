# 260224_speed_test_result-4.md

## conditions
- ESP32-S3(host) - ESP32-S3(client)
- pio-ESP32S3-Serial-WiFi-Bridge - pio-ESP32S3-Serial-WiFi-Client-Kerberos

## test1, uart2-com18(host) -> uart2-com29(client), flow control: enabled
- Average 82000 bps, max 108000 bps, min 3500 bps

```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py 
3538.78 bps                                                                             
32671.13 bps
77831.97 bps
50005.55 bps
58108.27 bps
59497.78 bps
66487.22 bps
23099.88 bps
38286.39 bps
70974.22 bps
77033.33 bps
80240.13 bps
78274.95 bps
85029.61 bps
80010.75 bps
79048.20 bps
96127.66 bps
89747.27 bps
88844.89 bps
89882.67 bps
96622.58 bps
87002.68 bps
101059.81 bps
105203.01 bps
99724.88 bps
97454.75 bps
102391.41 bps
106546.77 bps
108124.37 bps
87587.94 bps
91371.89 bps
41076.35 bps
78954.53 bps
79964.78 bps
99334.86 bps
67170.67 bps
70372.86 bps
78913.38 bps
78724.66 bps
86967.95 bps
78917.57 bps
79282.09 bps
79094.87 bps
76795.18 bps
88044.04 bps
88784.61 bps
96418.29 bps
96521.74 bps
99536.73 bps
100045.17 bps
95527.63 bps
104900.18 bps
100113.71 bps
48213.42 bps
99794.33 bps
103437.76 bps
101754.82 bps
97536.30 bps
```

## test2, uart2-com18(host) <- uart2-com29(client), flow control: enabled
- Average 20000 bps, max 45000 bps, min 3000 bps

```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
3093.23 bps
45183.01 bps
13730.60 bps
27579.84 bps
16415.60 bps
19765.85 bps
13921.65 bps
16426.43 bps
35207.73 bps
13605.49 bps
13789.07 bps
27787.25 bps
27249.54 bps
13880.87 bps
13761.62 bps
19383.92 bps
27522.93 bps
13814.08 bps
13635.89 bps
13772.15 bps
13753.68 bps
13736.68 bps
32545.46 bps
13737.50 bps
27304.04 bps
13780.52 bps
27373.26 bps
13823.80 bps
16385.23 bps
```

## test3, uart2-com18(host) -> uart2-com29(client), flow control: disabled

```
```

## test4, uart2-com18(host) <- uart2-com29(client), flow control: disabled

```
```
