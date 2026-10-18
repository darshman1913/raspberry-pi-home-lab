# Add a WireGuard Peer

## When you need this

Use this to give a new device VPN access to the home network. Right now there are two peers: the Windows laptop on `10.0.0.2` and the iPhone on `10.0.0.3`. Adding more clients is on the WireGuard next steps list.

The steps below use `tablet` as the example device name and `10.0.0.4` as its tunnel IP.

## Steps

1. SSH into the Pi. Use `192.168.1.165` from home or `10.0.0.1` through the VPN.

    ```bash
    ssh username@192.168.1.165
    ```

2. Generate a keypair for the new device.

    ```bash
    cd /etc/wireguard
    sudo wg genkey | sudo tee tablet_private.key | wg pubkey | sudo tee tablet_public.key
    ```

3. Back up the server config before editing it.

    ```bash
    sudo cp /etc/wireguard/wg0.conf /etc/wireguard/wg0.conf.bak
    ```

4. Add a peer block to the server config with the new public key and the next free tunnel IP.

    ```bash
    sudo nano /etc/wireguard/wg0.conf
    ```

    ```ini
    [Peer]
    PublicKey = TABLET_PUBLIC_KEY
    AllowedIPs = 10.0.0.4/32
    ```

5. Create the client config. Same shape as the iPhone one.

    ```ini
    [Interface]
    PrivateKey = TABLET_PRIVATE_KEY
    Address = 10.0.0.4/24
    DNS = 192.168.1.165

    [Peer]
    PublicKey = SERVER_PUBLIC_KEY
    Endpoint = PUBLIC_IP:51820
    AllowedIPs = 0.0.0.0/0
    PersistentKeepalive = 25
    ```

6. Get the config onto the device. For a phone or tablet, show a QR code and scan it with the WireGuard app.

    ```bash
    qrencode -t ansiutf8 < tablet.conf
    ```

    For a laptop, import the file into the WireGuard app.

7. Restart WireGuard so it loads the new peer.

    ```bash
    sudo systemctl restart wg-quick@wg0
    ```

    This drops your SSH session. Reconnect.

## Verify

Connect from the new device, then on the Pi:

```bash
sudo wg show
```

The new peer should have a latest handshake. From the new device, `nslookup google.com` should show `192.168.1.165` as the DNS server.

## What can go wrong

* **Permission denied creating keys.** Run `wg genkey` with `sudo`. Same issue I hit during the first build.
* **Reused tunnel IP.** Two peers with the same `AllowedIPs` will fight and one of them stops working. Check the existing peers in `wg0.conf` first.
* **No handshake.** Check the router port forward first: UDP, 51820, `192.168.1.165`. When this happened before, the problem was the router and not WireGuard.
* **Leaked keys or QR code.** Never share private keys, full configs, or QR codes after deployment. If one leaks, generate a new keypair, update the peer, and remove the old key.
