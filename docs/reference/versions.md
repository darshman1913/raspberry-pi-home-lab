# Versions and Hardware

Hardware and software versions from the three builds. The full Lab Environment table from each project is below the summary.

## At a Glance

| Item | Version |
| ---- | ------- |
| Raspberry Pi | Raspberry Pi 5, 8GB |
| Operating System | Raspberry Pi OS 64-bit, based on Debian |
| Router | Verizon CR1000A |
| Management Device | Windows laptop |
| Pi-hole Core | v6.4.2 |
| Pi-hole FTL | v6.6.2 |
| Pi-hole Web Interface | v6.5 |
| WireGuard | 1.0.20210914 |
| Cowrie | 3.0.3 |
| Python (Cowrie) | 3.13.5 |

The docs site itself was built on the Windows laptop with Python 3.14.3, Zensical 0.0.71, diagrams 0.25.1, and Graphviz 16.1.0.

## 01 - Pi-hole DNS Sinkhole

| Component             | Details                                |
| --------------------- | -------------------------------------- |
| Hardware              | Raspberry Pi 5                         |
| Operating System      | Raspberry Pi OS 64-bit based on Debian |
| Router                | Verizon CR1000A                        |
| Management Device     | Windows laptop                         |
| Pi-hole Core          | v6.4.2                                 |
| Pi-hole FTL           | v6.6.2                                 |
| Pi-hole Web Interface | v6.5                                   |
| Upstream DNS          | Cloudflare `1.1.1.1` with DNSSEC       |
| Blocklist Size        | 83,497 domains                         |
| Active Clients        | 5 devices                              |
| Blocking Rate         | Around 8% to 45% of DNS traffic        |
| Pi Static IP          | `192.168.1.165`                        |
| Remote Access         | SSH from Windows laptop                |

## 02 - WireGuard VPN Server

| Component           | Details                         |
| ------------------- | ------------------------------- |
| Hardware            | Raspberry Pi 5                  |
| Operating System    | Raspberry Pi OS 64-bit (Debian) |
| WireGuard Version   | 1.0.20210914                    |
| Router              | Verizon CR1000A                 |
| Server LAN IP       | 192.168.1.165                   |
| VPN Tunnel Network  | 10.0.0.0/24                     |
| WireGuard Server IP | 10.0.0.1                        |
| Listen Port         | UDP 51820                       |
| VPN DNS Server      | Pi-hole (192.168.1.165)         |
| Routing Mode        | Full Tunnel                     |
| Windows Client IP   | 10.0.0.2                        |
| iPhone Client IP    | 10.0.0.3                        |
| Public IP           | Redacted                        |
| Remote Access       | WireGuard VPN                   |

## 03 - Cowrie SSH Honeypot

| Component       | Details                |
| --------------- | ---------------------- |
| Hardware        | Raspberry Pi 5         |
| OS              | Raspberry Pi OS 64-bit |
| Cowrie Version  | 3.0.3                  |
| Python Version  | 3.13.5                 |
| Hostname        | ubuntu-server          |
| Router          | Verizon CR1000A        |
| External Port   | 22                     |
| Internal Port   | 2222                   |
| Service Account | cowrie                 |
| Startup Method  | systemd                |
| Log Formats     | JSON + plaintext       |
| Dashboard       | Custom HTML/JavaScript |
