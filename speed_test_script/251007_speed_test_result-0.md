# 251007_speed_test_result-0.md

## test1
- Host -> Client: around 11000 bps, 1/10
- Client -> Host: around 80000 bps

### test1 detail
- Host -> Client: around 11000 bps, 1/10
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
9437.34 bps
10642.07 bps
6163.63 bps
14873.13 bps
11102.08 bps
11005.70 bps
5552.57 bps
10833.07 bps
11031.34 bps
5211.61 bps
5783.82 bps
16435.98 bps
10812.21 bps
9828.91 bps
12238.48 bps
5398.71 bps
11187.61 bps
```
- Client -> Host: around 80000 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
76537.87 bps
80721.85 bps
80845.42 bps
80787.46 bps
81025.16 bps
80693.60 bps
80843.86 bps
80668.67 bps
80694.41 bps
80951.30 bps
80942.55 bps
80923.27 bps
80717.47 bps
```

## test2
- Host -> Client, around 11000 bps, 1/10
- Client -> Host, around 115200 bps, Ok

### test2, detail
- Host -> Client, around 11000 bps, 1/10
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
8613.45 bps
7017.59 bps
13569.80 bps
6700.04 bps
13826.51 bps
14297.73 bps
13348.43 bps
13311.04 bps
13815.43 bps
6572.14 bps
```
- Client -> Host, around 115200 bps, Ok
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
2490.32 bps
103051.81 bps
101330.02 bps
101190.01 bps
101395.86 bps
101285.53 bps
101177.61 bps
101078.65 bps
101285.08 bps
100570.91 bps
100694.02 bps
```

## test3
- Host -> Client, around 115200 bps
- Client -> Host, around 13000 bps, 1/10

### test3, detail
- Host -> Client, around 115200 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
825.76 bps
101699.98 bps
101086.60 bps
100784.28 bps
101176.80 bps
101184.19 bps
101181.45 bps
100977.22 bps
101200.93 bps
101220.15 bps
```
- Client -> Host, around 13000 bps, 1/10
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
8643.42 bps
13705.61 bps
7663.88 bps
13088.96 bps
12960.40 bps
13315.06 bps
14086.15 bps
13497.89 bps
14034.07 bps
13409.55 bps
```
