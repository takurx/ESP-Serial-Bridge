# 251218_speed_test_result-3.md

## result3
- Host -> Client: around 13000 bps, たまに7000 pbs
- Client -> Host: around 100000 bps, 安定

### test3-1
- Host -> Client: around 13000 bps, たまに7000 pbs
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
2329.42 bps
16523.34 bps
13072.70 bps
14283.74 bps
13004.31 bps
13610.43 bps
15456.41 bps
12438.58 bps
7194.69 bps
14002.30 bps
12974.87 bps
13865.76 bps
13491.13 bps
6765.28 bps
13316.72 bps
7418.59 bps
```

### test3-2
- Client -> Host: around 100000 bps, 安定
```
PS C:\250602_Works\250602_GitLab\ESP-Serial-Bridge\speed_test_script> python .\test1_receive_random.py
2272.60 bps
100997.60 bps
101210.61 bps
100990.90 bps
101178.83 bps
100955.79 bps
101211.82 bps
101224.42 bps
101149.83 bps
101099.87 bps
101183.12 bps
101104.42 bps
101218.29 bps
101217.81 bps
101093.97 bps
101109.94 bps
101140.87 bps
101307.08 bps
```
