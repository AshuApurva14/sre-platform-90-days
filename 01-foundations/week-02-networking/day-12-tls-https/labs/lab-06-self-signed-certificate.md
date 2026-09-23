# Lab 6: Create your own certificate

Now things become much more interesting.

Create:

```bash
mkdir -p ~/tls-lab
cd ~/tls-lab
```

Generate private key:

```bash
openssl genrsa -out server.key 2048
```

Check:

```bash
ls -l
```

You should have:

`server.key`

Generate self-signed certificate:

```bash
openssl req \
  -x509 \
  -new \
  -key server.key \
  -sha256 \
  -days 365 \
  -out server.crt \
  -subj "/CN=localhost"
```

Now:

```bash
ls -l
```

You should have:

```
server.key
server.crt
```

Understand:

```bash
server.key
     ↓
PRIVATE KEY
     ↓
KEEP SECRET
```
```
server.crt
     ↓
CERTIFICATE
     ↓
Can be presented to clients
```

Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ mkdir -p ~/tls-lab
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ mkdir tls-lab
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ cd tls-lab/
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ 
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ openssl genrsa -out server.key 2048
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ 
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ ls -la
total 4
drwxrwxrwx 1 ashu ashu 4096 Sep 23 02:48 .
drwxrwxrwx 1 ashu ashu 4096 Sep 23 02:48 ..
-rwxrwxrwx 1 ashu ashu 1704 Sep 23 02:49 server.key
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ openssl req -x509 -new -key server.key -sha256 -days 365 -out server.crt -subj "/CN=localhost"
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ 
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ ls -l
total 8
-rwxrwxrwx 1 ashu ashu 1115 Sep 23 02:51 server.crt
-rwxrwxrwx 1 ashu ashu 1704 Sep 23 02:49 server.key
```

Inspect it:

```bash
openssl x509 \
  -in server.crt \
  -text \
  -noout
```

Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ openssl x509 -in server.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            31:70:51:a9:19:95:be:54:67:0c:d1:f4:2b:90:c8:df:e2:64:e8:4d
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = localhost
        Validity
            Not Before: Sep 23 02:51:17 2026 GMT
            Not After : Sep 23 02:51:17 2027 GMT
        Subject: CN = localhost
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:c4:b6:d3:55:b5:32:e0:97:eb:85:a5:4e:d2:1f:
                    d3:81:ba:90:14:39:8c:fe:e3:4f:20:4d:f8:ee:7b:
                    1c:a1:04:7f:f3:00:32:f7:60:6c:0f:41:65:b6:4d:
                    27:95:c2:d9:48:7f:23:4c:8e:a1:34:e3:3d:1e:4e:
                    c7:c6:dd:26:b5:f9:18:19:85:d3:4a:63:26:fe:a1:
                    1a:b3:35:50:44:1d:ad:6d:af:29:cb:2e:2d:01:89:
                    a4:a3:49:08:9b:25:64:ad:29:98:a9:de:ab:3f:8d:
                    43:82:0d:39:ff:71:ef:8f:e0:93:e0:be:3b:23:15:
                    22:cd:3f:73:34:86:aa:3b:7e:25:d4:ba:49:9c:55:
                    22:98:eb:f0:ca:86:86:ed:08:fd:49:8e:63:53:be:
                    b6:a8:44:59:05:34:3b:6a:24:6c:11:7f:c9:fb:10:
                    66:4f:91:d4:7d:15:21:e2:e2:29:11:3e:c5:fc:30:
                    2c:b0:01:17:5b:97:1c:93:88:98:e1:24:c4:ef:b0:
                    0b:26:a4:58:5b:10:04:be:7e:1e:38:a5:87:e5:31:
                    0f:22:88:c3:92:2d:44:fe:ba:3b:b4:ab:62:d2:a6:
                    ff:52:6c:a0:7b:f4:c2:39:97:80:44:87:bf:6d:f9:
                    a9:6c:9f:7b:b3:b4:40:ba:3e:89:36:f2:05:db:25:
                    fe:55
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier: 
                ED:26:66:9A:20:63:40:77:D4:9A:A3:4F:61:51:36:F8:76:33:CD:EE
            X509v3 Authority Key Identifier: 
                ED:26:66:9A:20:63:40:77:D4:9A:A3:4F:61:51:36:F8:76:33:CD:EE
            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        5c:d3:9e:17:7f:08:46:99:ce:a7:a8:8a:82:eb:0b:c6:d7:89:
        b0:8d:37:0a:77:fa:50:90:a2:80:98:08:7a:01:a8:db:13:f4:
        15:bf:37:f5:52:c1:77:c2:0d:da:27:01:7e:30:86:72:7e:8d:
        a6:e2:15:97:bf:58:b6:90:69:16:3d:e7:5b:34:87:0a:ae:29:
        f3:e8:3a:cf:92:97:a1:6f:95:99:2d:05:3c:3f:ae:28:f8:6c:
        2a:54:5b:09:d6:c9:d0:85:53:31:37:d9:f9:e0:c4:0f:47:5f:
        19:56:bc:a2:7f:28:cd:1a:a7:29:35:c2:a1:e3:02:a3:2c:01:
        04:1f:c1:c3:10:32:61:35:e3:d8:41:15:6a:a9:f6:6c:d0:c1:
        55:3b:cc:7d:99:7b:b9:50:a3:7c:83:74:1b:10:d2:1a:c4:ba:
        d9:ad:9c:6e:4c:a8:4b:3b:05:84:2c:7f:90:16:51:41:6c:8d:
        93:d4:3c:09:48:f0:33:ce:11:8e:52:4c:21:60:a3:10:ea:4b:
        a4:6d:05:f7:be:07:80:76:37:fb:8e:3b:72:39:43:d1:eb:0b:
        40:cb:d9:7c:64:cd:a1:e1:1d:4e:36:ed:24:80:07:e8:e9:bb:
        59:6c:e9:89:8b:34:6e:cf:50:e9:a4:4f:e7:18:12:c6:9b:99:
        ac:dd:9f:d4
ashu@DESKTOP-ITELHM3:
```

