# DNS TCP TLS HTTP 


| Layer   | Question                         | Main Tool                |
| ------- | -------------------------------- | ------------------------ |
| DNS     | Can hostname resolve?            | `dig`                    |
| Routing | Can traffic reach destination?   | `ip route`, `traceroute` |
| TCP     | Can port accept connection?      | `nc`, `ss`               |
| TLS     | Can secure connection establish? | `openssl`, `curl -v`     |
| HTTP    | What did application return?     | `curl`                   |

