# Force Clients to Renew DHCP Leases

## When you need this

Use this after DHCP moves between the router and Pi-hole, or after changing the DHCP range or DNS settings in Pi-hole.

I needed this after the switch to Pi-hole DHCP. Some devices still had old leases from the router, so they did not show up in Pi-hole right away. DHCP changes are not instant. Clients hold their old lease until they renew or reconnect.

## Steps

1. On Windows, open PowerShell and release the current lease.

    ```powershell
    ipconfig /release
    ```

2. Ask for a new one.

    ```powershell
    ipconfig /renew
    ```

3. On phones and TVs, disconnect from Wi-Fi and reconnect.

4. For anything without a network menu, power cycle it.

## Verify

On Windows:

```powershell
ipconfig /all
```

With Pi-hole running DHCP, the DHCP server and DNS server should both be `192.168.1.165`, and the address should be inside `192.168.1.100` to `192.168.1.250`.

In the Pi-hole dashboard, the device should show up as an active client. With everything renewed I had 5.

## What can go wrong

* **You lose your connection to the machine.** `ipconfig /release` drops the network on that machine until `/renew` finishes. Do not run it on a machine you are connected to remotely.
* **Two DHCP servers are on.** If the router DHCP is still enabled, devices can get a lease from either one. Check that the Verizon CR1000A DHCP is disabled.
* **The device has DNS set by hand.** A manual DNS setting overrides what DHCP hands out, so the device skips Pi-hole. Set the adapter back to automatic.
* **Renew times out.** The Pi may be unreachable. SSH in and check its address with `hostname -I`. It should be `192.168.1.165`.
