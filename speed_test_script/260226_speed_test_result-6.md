# 260226_speed_test_result-6.md
- flow controlなし
- host -> client x3, around 13000 bps
- host <- client x3, around 10000 bps

## host -> client x3
- average 13967 bps

- com3 -> com24
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com24.py
7596.18 bps
7175.18 bps
19639.19 bps
18791.18 bps
8122.44 bps
13517.37 bps
12444.75 bps
14206.08 bps
15386.03 bps
12497.33 bps
18692.37 bps
8009.68 bps
10245.09 bps
19383.14 bps
20283.87 bps
25798.97 bps
7614.46 bps
12179.18 bps
13659.21 bps
14593.62 bps
6545.90 bps
14955.96 bps
```

- com6 -> com26
- average 13284 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com26.py
8855.64 bps
14918.95 bps
12900.29 bps
13026.45 bps
8224.27 bps
11504.15 bps
14826.84 bps
20563.80 bps
12833.26 bps
20899.39 bps
14135.63 bps
12717.04 bps
7341.20 bps
14701.79 bps
23033.34 bps
8126.93 bps
14004.12 bps
12100.98 bps
13705.73 bps
8408.98 bps
11714.63 bps
13713.57 bps
```

- com11 -> com25
- average 13502 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com25.py
13206.13 bps
13775.84 bps
12421.58 bps
7115.57 bps
23068.78 bps
12448.88 bps
14314.66 bps
14793.40 bps
16774.85 bps
15289.52 bps
14034.05 bps
12244.31 bps
7660.88 bps
14175.22 bps
19352.01 bps
14613.88 bps
7306.85 bps
17434.52 bps
7816.88 bps
19367.18 bps
6336.11 bps
```

## host <- client x3
- com3 <- com24
- average 9681 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com3.py 
8901.60 bps
7997.97 bps
11294.82 bps
7786.55 bps
6516.94 bps
14254.28 bps
7356.33 bps
12117.76 bps
7438.99 bps
12072.86 bps
14020.42 bps
7028.32 bps
6895.26 bps
13940.02 bps
6530.36 bps
13070.82 bps
8446.79 bps
12321.16 bps
7261.39 bps
12345.44 bps
7917.43 bps
12410.51 bps
6855.78 bps
7573.46 bps
```

- com6 <- com26
- average 9661 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com6.py 
13171.98 bps
6387.59 bps
6977.85 bps
7815.86 bps
12015.40 bps
7368.00 bps
7171.76 bps
17781.45 bps
7190.08 bps
7254.44 bps
14234.08 bps
12990.19 bps
6289.10 bps
7747.92 bps
13075.14 bps
13674.24 bps
6261.42 bps
7250.77 bps
7264.03 bps
19895.93 bps
6244.38 bps
6862.85 bps
7288.81 bps
```

- com11 <- com25
- average 9898 bps
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random_com11.py
8809.17 bps
7930.15 bps
12917.67 bps
7220.33 bps
12540.10 bps
7058.84 bps
7330.00 bps
17718.81 bps
7344.16 bps
6985.82 bps
6799.95 bps
7366.29 bps
16610.63 bps
7271.77 bps
7397.20 bps
7422.21 bps
17724.66 bps
7355.78 bps
6795.71 bps
7430.07 bps
19842.56 bps
```
