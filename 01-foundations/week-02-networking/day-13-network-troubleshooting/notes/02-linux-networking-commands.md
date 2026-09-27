# Most common  Linux networking commands

```bash
ip
ss
ping
traceroute
tracepath
dig
nslookup
host
nc
curl
openssl
tcpdump

```

**Why we need these commands?**

You want to know how these commands helps in troubleshooting:

## `ip` Command

**WHAT?**

 *It is used to configure and manage network devices, interfaces and route tables.*

**WHY?**


- Does the machine have an IP?
- Which interface?
- Is it UP?
- Is route table has particular IP route?
- How many network devices are connected to the machine?


**HOW?**

Below are the most common used commands:

- `ip addr` or `ip a` - To show addresses assigned to all network interfaces.

- `ip route` - Check route

```bash
    ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ip route 
    default via 192.168.96.1 dev eth0 proto kernel 
    172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
    192.168.96.0/20 dev eth0 proto kernel scope link src 192.168.105.235 
```

```
default via ...

This is the default gateway.
```

```
   Destination
       |
    Gateway
       |
    Interfaces
```

## `ss` (Socket Statistics)

 Show listening ports or examine sockets.

Without process:

```bash
   ss -lnt
```

With process:

```bash
 ss -lntp
 ```

Meaning:
 ```
l - listening
n - numeric
t - TCP
p - process
 ```

 Example:
 
 ```
 LISTEN 0 128 0.0.0.0:8080
 ```
 Means something is listening over port 8080.

 `ss ant` - 

Show established connections

Example:

It shows `state` of the sockets

```bash
ss -ant
```


You may see Output like:

```bash
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ss -ant
State                         Recv-Q                        Send-Q                                                Local Address:Port                                                Peer Address:Port                        Process                        
LISTEN                        0                             4096                                                     127.0.0.54:53                                                       0.0.0.0:*                                                          
LISTEN                        0                             1000                                                 10.255.255.254:53                                                       0.0.0.0:*                                                          
LISTEN                        0                             511                                                         0.0.0.0:80                                                       0.0.0.0:*                                                          
LISTEN                        0                             4096                                                  127.0.0.53%lo:53                                                       0.0.0.0:*                                                          
LISTEN                        0                             511                                                            [::]:80                                                          [::]:*                                                          
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ 
```

Notice the first column `State` above:

```bash
State
ESTAB
LISTEN
TIME-WAIT
CLOSE-WAIT
```

## `ping`

Send ICMP ECHO_REQUEST to network hosts. It uses ICMP protocol to transmit echo request.

```
Source (Client)                                   Destination (Server)

      |                                                     |
      |--- 1. ICMP Echo Request (Type 8)------------------>|
      |    (Contains Source IP, Destination IP)             |
      |                                                     |
      |    <-- 2. Processing Request (OS/Network Stack) ----|
      |                                                     |
      |<-- 3. ICMP Echo Reply (Type 0) ---------------------|
      |    (Reverses Source/Destination IPs)                |
      |                                                     |
      |--- 4. Calculate Round-Trip Time (RTT) & Display --->|

```

`ICMP` - It is network layer protocol used by network devices to diagnose communication issues and send error messages.

Example:

```bash

ping google.com
```

## `traceroute`

It is network troubleshooting tool used to trace path of the packets sent over network from source to destination.

It attempts to show path:

```
Your machine
 ↓
Gateway
 ↓
Router
 ↓
Router
 ↓
Router
 ↓
Destination
```

Example:

```bash
traceroute google.com
```
Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ traceroute google.com
traceroute to google.com (142.250.118.102), 64 hops max
  1   192.168.96.1  0.430ms  1.240ms  1.034ms 
  2   192.168.31.1  79.380ms  3.208ms  3.219ms 
  3   192.0.0.1  4.268ms  3.298ms  2.816ms 
  4   192.0.0.1  28.912ms  23.967ms  19.281ms 
  5   192.0.0.1  32.561ms  25.326ms  22.810ms 
  6   192.0.0.1  20.603ms  19.440ms  26.159ms 
  7   192.168.227.131  38.468ms  15.266ms  25.007ms 
  8   192.168.173.4  15.809ms  192.168.173.6  19.022ms  192.168.173.4  20.133ms 
  9   192.168.173.7  22.683ms  18.946ms  25.595ms 
 10   172.31.6.133  24.864ms  41.867ms  35.389ms 
 11   172.31.5.107  56.913ms  64.159ms  55.456ms 
 12   *  142.251.201.128  54.884ms  49.300ms 
 13   142.251.76.107  53.612ms  45.665ms  45.192ms 
 14   142.251.76.174  56.441ms  43.319ms  49.956ms 
 15   142.251.66.229  60.170ms  58.220ms  48.303ms 
 16   108.170.241.230  48.908ms  48.306ms  55.671ms 
 17   *  *  * 
 18   *  *  * 
 19   *  *  * 
 20   *  *  * 
 21   *  *  * 
 22   *  *  * 
 23   *  *  * 
 24   142.250.118.102  48.621ms  43.657ms  47.367ms 
 ```

**NOTE:** 

On some networks, intermediate hops may not respond, so * * * doesn't automatically mean the destination is broken. See above 

## `tracepath`

- It is also used for trace path of the packets sent over network from source to destination.

- It can help identify routing/path and MTU-related information.

Example:

```bash

tracepath google.com
```

Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ tracepath google.com
 1?: [LOCALHOST]                      pmtu 1500
 1:  LAPTOP-ASHU.mshome.net                                0.811ms 
 1:  LAPTOP-ASHU.mshome.net                                0.294ms 
 2:  jiofiber.local.html                                   8.009ms 
 3:  192.0.0.1                                             5.449ms 
 4:  192.0.0.1                                             3.389ms pmtu 1480
 4:  192.0.0.1                                            25.500ms 
 5:  192.0.0.1                                            27.025ms asymm  6 
 6:  192.0.0.1                                            21.973ms asymm  7 
 7:  192.168.227.130                                      26.469ms asymm  8 
 8:  192.168.173.6                                        24.285ms asymm  9 
 9:  192.168.173.7                                        29.260ms 
10:  172.31.6.135                                         37.668ms 
11:  172.31.5.109                                         46.464ms asymm 10 
12:  72.14.195.34                                         46.057ms asymm 15 
13:  no reply
14:  no reply
15:  no reply
16:  no reply
17:  no reply
18:  no reply
19:  no reply
It can help identify routing/path and MTU-related information.20:  no reply
21:  no reply
22:  no reply
23:  no reply
24:  no reply
25:  no reply
26:  no reply
27:  no reply
28:  no reply
29:  no reply
30:  no reply
     Too many hops: pmtu 1480
     Resume: pmtu 1480
```

## `netcat`

- It is used for port scanning for TCP , UDP or unix domain sockets.

This tells you:

```
DNS -> resolved
TCP -> reachable
Port 443 -> accept connection
```
It does not prove:

```
TLS works
HTTP works
Application works
```

## `curl`

- `curl` is a tool for transferring data from or to a server using URLs.
- It supports protocols such as HTTP, HTTPS, FTP, SMTP, SFTP,SCP, TELNET etc.
- It is useful for perfomance troubleshooting.

This gives you:

```
DNS
TCP
TLS
HTTP
```
Example:

```
curl -v https://httpbin.org
```

