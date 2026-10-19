# Network Map

Every IP, subnet, and port used across the lab. LAN means it only exists inside my home network. Public means it is reachable from the internet. VPN means it only exists inside the WireGuard tunnel.

| Address or port | What it is | Scope | Project |
| --------------- | ---------- | ----- | ------- |
| `192.168.1.0/24` | Home LAN subnet | LAN | 01 |
| `192.168.1.1` | Gateway, Verizon CR1000A | LAN | 01 |
| `192.168.1.165` | Raspberry Pi 5 static IP. Pi-hole DNS and DHCP, WireGuard, Cowrie | LAN | 01, 02, 03 |
| `192.168.1.100` to `192.168.1.250` | Pi-hole DHCP range | LAN | 01 |
| `http://192.168.1.165/admin` | Pi-hole web dashboard | LAN | 01 |
| `1.1.1.1`, `1.0.0.1` | Upstream DNS, Cloudflare with DNSSEC | Public | 01 |
| Public IP | Home internet address | Public | 02 |
| UDP `51820` | WireGuard listen port, forwarded by the router to `192.168.1.165` | Public | 02 |
| `10.0.0.0/24` | WireGuard tunnel network | VPN | 02 |
| `10.0.0.1` | WireGuard server, also used for SSH through the tunnel | VPN | 02 |
| `10.0.0.2` | Windows laptop client | VPN | 02 |
| `10.0.0.3` | iPhone client | VPN | 02 |
| TCP `22` | Cowrie external port, forwarded by the router to `2222` | Public | 03 |
| TCP `2222` | Cowrie internal listen port on the Pi | LAN | 03 |

The public IP is redacted on purpose. See the security notes in [Explanation](../explanation/index.md#security-notes).

VPN clients use `192.168.1.165` as their DNS server, so Pi-hole filtering still applies when I am away from home.

## Final Working Results

### 01 - Pi-hole DNS Sinkhole

Current working status:

| Item                    | Result            |
| ----------------------- | ----------------- |
| Pi-hole Running         | Yes               |
| Web Dashboard Working   | Yes               |
| DNS Filtering Working   | Yes               |
| DHCP Running on Pi-hole | Yes               |
| Router DHCP Disabled    | Yes               |
| Active Clients          | 5                 |
| Static IP Working       | Yes               |
| Cloudflare Upstream DNS | Yes               |
| DNSSEC Enabled          | Yes               |
| Blocklist Domains       | 83,497            |
| Blocking Rate           | Around 8% to 45%  |
| `doubleclick.net` Test  | Returns `0.0.0.0` |

### 02 - WireGuard VPN Server

| Item                    | Status |
| ----------------------- | ------ |
| WireGuard Running       | Yes    |
| Port Forwarding Working | Yes    |
| Laptop Client Connected | Yes    |
| iPhone Client Connected | Yes    |
| Full Tunnel Routing     | Yes    |
| Pi-hole DNS Through VPN | Yes    |
| SSH Through Tunnel      | Yes    |
| Handshakes Verified     | Yes    |
| Encryption Active       | Yes    |
