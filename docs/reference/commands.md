# Command Reference

Every command from the three projects, grouped by service. Pi commands run over SSH on the Raspberry Pi. Windows commands run in PowerShell on the laptop.

## Raspberry Pi OS

### System Update

```bash
sudo apt update
sudo apt full-upgrade -y
```

### Reboot Raspberry Pi

```bash
sudo reboot
```

### Check Raspberry Pi IP Address

```bash
hostname -I
```

### Edit Static IP Configuration

```bash
sudo nano /etc/dhcpcd.conf
```

## Pi-hole

### Install Pi-hole

```bash
curl -sSL https://install.pi-hole.net | bash
```

### Check Pi-hole Status

```bash
pihole status
```

### View Live DNS Queries

```bash
pihole -t
```

### Update Gravity / Blocklists

```bash
pihole -g
```

### Restart Pi-hole DNS

```bash
pihole restartdns
```

### Change Pi-hole Admin Password

```bash
pihole setpassword
```

### Check Pi-hole Version

```bash
pihole -v
```

### Repair Pi-hole Installation

```bash
pihole -r
```

### Flush Pi-hole Logs

```bash
pihole flush
```

## Windows Client

### Windows: Release IP Lease

```powershell
ipconfig /release
```

### Windows: Renew IP Lease

```powershell
ipconfig /renew
```

### Windows: Check Network Details

```powershell
ipconfig /all
```

### Windows: Test Blocked Domain

```powershell
nslookup doubleclick.net
```

Expected blocked result:

```text
Address: 0.0.0.0
```

## WireGuard

### Show Status

```bash
sudo wg show
```

### Start WireGuard

```bash
sudo systemctl start wg-quick@wg0
```

### Stop WireGuard

```bash
sudo systemctl stop wg-quick@wg0
```

### Restart WireGuard

```bash
sudo systemctl restart wg-quick@wg0
```

### Enable at Boot

```bash
sudo systemctl enable wg-quick@wg0
```

### Check Service

```bash
sudo systemctl status wg-quick@wg0
```

### Show IP Forwarding

```bash
sysctl net.ipv4.ip_forward
```

### View Configuration

```bash
sudo cat /etc/wireguard/wg0.conf
```

### Generate QR Code

```bash
qrencode -t ansiutf8 < iphone.conf
```

## Cowrie

The log paths are relative to the cloned `cowrie` folder.

### Service Status

```bash
sudo systemctl status cowrie
```

### Start Service

```bash
sudo systemctl start cowrie
```

### Stop Service

```bash
sudo systemctl stop cowrie
```

### Restart Service

```bash
sudo systemctl restart cowrie
```

### Follow Logs

```bash
tail -f var/log/cowrie/cowrie.log
```

### JSON Events

```bash
tail -f var/log/cowrie/cowrie.json
```

### Switch to Cowrie User

```bash
sudo -u cowrie -s
```
