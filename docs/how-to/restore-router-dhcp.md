# Restore DHCP to the Verizon Router

## When you need this

Use this if you want the Verizon CR1000A to hand out IP addresses again. For example if the Pi is down, if you are troubleshooting the router, or if you are tearing the lab down.

The tradeoff: devices will go back to using the router for DNS. That means DNS filtering stops working until you point them at the Pi manually.

## Steps

1. Log into the Pi over SSH.

    ```bash
    ssh myusername@192.168.1.165
    ```

2. Disable DHCP on Pi-hole. In the web dashboard: Settings > DHCP > uncheck DHCP server enabled > Save.

3. Log into the Verizon CR1000A admin page.

4. Turn DHCP back on. Advanced > IP Address Distribution or the equivalent menu on your firmware.

5. Reboot the Pi so it picks up a lease from the router instead of handing one to itself.

    ```bash
    sudo reboot
    ```

## Verify

On a Windows machine, release and renew:

```powershell
ipconfig /release
ipconfig /renew
ipconfig /all
```

The default gateway and DHCP server should now be the router, not the Pi.

## What can go wrong

* **Two DHCP servers running at once.** If you enable the router before disabling Pi-hole, you can get IP conflicts. Disable Pi-hole first.
* **The Pi loses network access mid changeover.** This is expected. The static IP in `dhcpcd.conf` brings it back after reboot.
* **Devices keep old leases.** Renew them or reconnect Wi-Fi. See [Force clients to renew DHCP leases](renew-client-leases.md).
