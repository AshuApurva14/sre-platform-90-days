# Lab 1 — Network Basics

## Objective

Understand how Linux networking information can be inspected.

## Commands

- `ip addr`
- `ip route`
- `ss -lntp`
- `ping`
- `traceroute `
- `nc -vz httpbin.org 443`
- `curl -v https://httpbin.org`

## Observations

Below are the observations for commands:

```
#  IP ADDR

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ip addr 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:0d:4d:61 brd ff:ff:ff:ff:ff:ff
    inet 192.168.105.235/20 brd 192.168.111.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe0d:4d61/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether fa:7c:f0:bf:a6:f1 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever


# IP ROUTE

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ip route
default via 192.168.96.1 dev eth0 proto kernel 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
192.168.96.0/20 dev eth0 proto kernel scope link src 192.168.105.235 


# SS -LNTP

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ss -lntp
State                         Recv-Q                         Send-Q                                                  Local Address:Port                                                 Peer Address:Port                        Process                        
LISTEN                        0                              511                                                           0.0.0.0:80                                                        0.0.0.0:*                                                          
LISTEN                        0                              4096                                                       127.0.0.54:53                                                        0.0.0.0:*                                                          
LISTEN                        0                              1000                                                   10.255.255.254:53                                                        0.0.0.0:*                                                          
LISTEN                        0                              4096                                                    127.0.0.53%lo:53                                                        0.0.0.0:*                                                          
LISTEN                        0                              511                                                              [::]:80                                                           [::]:*                                                          


# PING 

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ping -c 4 httpbin.org
PING httpbin.org (13.216.58.208) 56(84) bytes of data.
^C
--- httpbin.org ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3057ms


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ping -c 5 google.com
PING google.com (142.250.29.100) 56(84) bytes of data.
64 bytes from nw-in-f100.1e100.net (142.250.29.100): icmp_seq=1 ttl=107 time=49.2 ms
64 bytes from nw-in-f100.1e100.net (142.250.29.100): icmp_seq=2 ttl=107 time=53.6 ms
64 bytes from nw-in-f100.1e100.net (142.250.29.100): icmp_seq=3 ttl=107 time=50.3 ms
64 bytes from nw-in-f100.1e100.net (142.250.29.100): icmp_seq=4 ttl=107 time=54.7 ms
64 bytes from nw-in-f100.1e100.net (142.250.29.100): icmp_seq=5 ttl=107 time=56.0 ms

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4019ms
rtt min/avg/max/mdev = 49.168/52.755/55.970/2.593 ms

# TRACEROUTE

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ traceroute httpbin.org
traceroute to httpbin.org (54.172.131.225), 64 hops max
  1   192.168.96.1  0.514ms  0.394ms  0.316ms 
  2   192.168.31.1  4.778ms  3.037ms  2.077ms 
  3   192.0.0.1  4.698ms  10.987ms  3.066ms 
  4   192.0.0.1  28.262ms  35.324ms  22.330ms 
  5   192.0.0.1  21.878ms  23.147ms  31.883ms 
  6   192.0.0.1  13.920ms  19.345ms  25.602ms 
  7   192.168.227.131  27.268ms  18.237ms  18.823ms 
  8   192.168.173.2  27.753ms  192.168.173.0  22.648ms  24.452ms 
  9   192.168.173.5  33.085ms  13.954ms  20.506ms 
 10   172.31.6.133  31.197ms  40.009ms  23.954ms 
 11   172.31.2.71  48.438ms  48.574ms  49.922ms 
 12   103.198.140.174  56.092ms  56.673ms  56.065ms 
 13   103.198.140.195  281.640ms  252.632ms  338.467ms 
 14   *  *  * 
 15   *  *  * 
 16   *  *  * 
 17   *  *  * 
 18   *  * ^C

# NETCAT

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ nc -vz httpbin.org 443
Connection to httpbin.org (54.175.207.120) 443 port [tcp/https] succeeded!
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ curl -v https://httpbin.org
* Host httpbin.org:443 was resolved.
* IPv6: (none)
* IPv4: 18.213.21.177, 34.200.179.76, 54.172.131.225, 3.234.28.4, 107.21.166.194, 13.223.216.61, 3.217.138.231, 54.175.207.120
*   Trying 18.213.21.177:443...
* Connected to httpbin.org (18.213.21.177) port 443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256 / prime256v1 / rsaEncryption
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=httpbin.org
*  start date: Jun 19 00:00:00 2026 GMT
*  expire date: Jan  2 23:59:59 2027 GMT
*  subjectAltName: host "httpbin.org" matched cert's "httpbin.org"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M01
*  SSL certificate verify ok.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
*   Certificate level 1: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
*   Certificate level 2: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://httpbin.org/
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: httpbin.org]
* [HTTP/2] [1] [:path: /]
* [HTTP/2] [1] [user-agent: curl/8.5.0]
* [HTTP/2] [1] [accept: */*]
> GET / HTTP/2
> Host: httpbin.org
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/2 200 
< date: Sat, 26 Sep 2026 12:24:48 GMT
< content-type: text/html; charset=utf-8
< content-length: 9593
< server: gunicorn/19.9.0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< 
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>httpbin.org</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"
        rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">
    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }

        *,
        *:before,
        *:after {
            box-sizing: inherit;
        }

        body {
            margin: 0;
            background: #fafafa;
        }
    </style>
</head>

<body>
    <a href="https://github.com/requests/httpbin" class="github-corner" aria-label="View source on Github">
        <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"
            aria-hidden="true">
            <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
            <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"
                fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
            <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"
                fill="currentColor" class="octo-body"></path>
        </svg>
    </a>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position:absolute;width:0;height:0">
        <defs>
            <symbol viewBox="0 0 20 20" id="unlocked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z"></path>
            </symbol>

            <symbol viewBox="0 0 20 20" id="locked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8zM12 8H8V5.199C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="close">
                <path d="M14.348 14.849c-.469.469-1.229.469-1.697 0L10 11.819l-2.651 3.029c-.469.469-1.229.469-1.697 0-.469-.469-.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-.469-.469-.469-1.228 0-1.697.469-.469 1.228-.469 1.697 0L10 8.183l2.651-3.031c.469-.469 1.228-.469 1.697 0 .469.469.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c.469.469.469 1.229 0 1.698z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow">
                <path d="M13.25 10L6.109 2.58c-.268-.27-.268-.707 0-.979.268-.27.701-.27.969 0l7.83 7.908c.268.271.268.709 0 .979l-7.83 7.908c-.268.271-.701.27-.969 0-.268-.269-.268-.707 0-.979L13.25 10z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow-down">
                <path d="M17.418 6.109c.272-.268.709-.268.979 0s.271.701 0 .969l-7.908 7.83c-.27.268-.707.268-.979 0l-7.908-7.83c-.27-.268-.27-.701 0-.969.271-.268.709-.268.979 0L10 13.25l7.418-7.141z"
                />
            </symbol>


            <symbol viewBox="0 0 24 24" id="jump-to">
                <path d="M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.41L5.83 13H21V7z" />
            </symbol>

            <symbol viewBox="0 0 24 24" id="expand">
                <path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z" />
            </symbol>

        </defs>
    </svg>


    <div id="swagger-ui">
        <div data-reactroot="" class="swagger-ui">
            <div>
                <div class="information-container wrapper">
                    <section class="block col-12">
                        <div class="info">
                            <hgroup class="main">
                                <h2 class="title">httpbin.org
                                    <small>
                                        <pre class="version">0.9.2</pre>
                                    </small>
                                </h2>
                                <pre class="base-url">[ Base URL: httpbin.org/ ]</pre>
                            </hgroup>
                            <div class="description">
                                <div class="markdown">
                                    <p>A simple HTTP Request &amp; Response Service.
                                        <br>
                                        <br>
                                        <b>Run locally: </b>
                                        <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
                                    </p>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <a href="https://kennethreitz.org" target="_blank">the developer - Website</a>
                                </div>
                                <a href="mailto:me@kennethreitz.org">Send email to the developer</a>
                            </div>
                        </div>
                        <!-- ADDS THE LOADER SPINNER -->
                        <div class="loading-container">
                            <div class="loading"></div>
                        </div>

                    </section>
                </div>
            </div>
        </div>
    </div>


    <div class='swagger-ui'>
        <div class="wrapper">
            <section class="clear">
                <span style="float: right;">
                    [Powered by
                    <a target="_blank" href="https://github.com/rochacbruno/flasgger">Flasgger</a>]
                    <br>
                </span>
            </section>
        </div>
    </div>



    <script src="/flasgger_static/swagger-ui-bundle.js"> </script>
    <script src="/flasgger_static/swagger-ui-standalone-preset.js"> </script>
    <script src='/flasgger_static/lib/jquery.min.js' type='text/javascript'></script>
    <script>

        window.onload = function () {
            

            fetch("/spec.json")
                .then(function (response) {
                    response.json()
                        .then(function (json) {
                            var current_protocol = window.location.protocol.slice(0, -1);
                            if (json.schemes[0] != current_protocol) {
                                // Switches scheme to the current in use
                                var other_protocol = json.schemes[0];
                                json.schemes[0] = current_protocol;
                                json.schemes[1] = other_protocol;

                            }
                            json.host = window.location.host;  // sets the current host

                            const ui = SwaggerUIBundle({
                                spec: json,
                                validatorUrl: null,
                                dom_id: '#swagger-ui',
                                deepLinking: true,
                                jsonEditor: true,
                                docExpansion: "none",
                                apisSorter: "alpha",
                                //operationsSorter: "alpha",
                                presets: [
                                    SwaggerUIBundle.presets.apis,
                                    // yay ES6 modules ↘
                                    Array.isArray(SwaggerUIStandalonePreset) ? SwaggerUIStandalonePreset : SwaggerUIStandalonePreset.default
                                ],
                                plugins: [
                                    SwaggerUIBundle.plugins.DownloadUrl
                                ],
            
            // layout: "StandaloneLayout"  // uncomment to enable the green top header
        })

        window.ui = ui

        // uncomment to rename the top brand if layout is enabled
        // $(".topbar-wrapper .link span").replaceWith("<span>httpbin</span>");
        })
    })
}
    </script>  <div class='swagger-ui'>
    <div class="wrapper">
        <section class="block col-12 block-desktop col-12-desktop">
            <div>

                <h2>Other Utilities</h2>

                <ul>
                    <li>
                        <a href="/forms/post">HTML form</a> that posts to /post /forms/post</li>
                </ul>

                <br />
                <br />
            </div>
        </section>
    </div>
</div>
</body>

* Connection #0 to host httpbin.org left intact
```

## Why?

- These are commands are useful in your devops scenarios and issues.
- It is necessary to use thes tools and commands to be able to fix and troubleshoot the issues.

## Learning

- I can able to troubleshoot the devops issues step by step.
- Fix issues related to DNS, port and TCP connections etc.
- The above listed commands are basic or most common used network troubleshooting tools/commands for troubleshooting and fetching information.
- It helps in find out details related to network , source, destinations, port, packet path, routes etc.
- By using these commands network issues and fixes can be done efficientlt.