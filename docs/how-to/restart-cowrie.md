# Restart Cowrie Safely

## When you need this

Use this after editing `cowrie.cfg`, after updating Cowrie, or when the dashboard stops showing new events.

Cowrie listens on `2222`, not on the real SSH port, so restarting it does not touch your own SSH session.

## Steps

1. SSH into the Pi with your admin account, not the `cowrie` user. The `cowrie` user has no sudo on purpose. If you are on the VPN, use `10.0.0.1`.

2. Check the current state.

    ```bash
    sudo systemctl status cowrie
    ```

3. If you changed the config, back it up first. Switch to the `cowrie` user and copy it from inside the cloned `cowrie` folder.

    ```bash
    sudo -u cowrie -s
    cp etc/cowrie.cfg etc/cowrie.cfg.bak
    exit
    ```

4. Restart the service.

    ```bash
    sudo systemctl restart cowrie
    ```

5. Check it again.

    ```bash
    sudo systemctl status cowrie
    ```

## Verify

The status should show the service as active. Then watch for new events from the `cowrie` folder:

```bash
tail -f var/log/cowrie/cowrie.json
```

New connections from the internet should start showing up. If you test it yourself from the LAN, your own IP ends up in the logs, so filter it out before any analysis.

## What can go wrong

* **The service will not start.** The standard Cowrie launcher did not work reliably under systemd for me. The unit has to point at `twistd` inside the virtual environment.
* **Old guides use `bin/cowrie`.** My version uses `cowrie-env/bin/cowrie`.
* **Permission errors.** Run `systemctl` from the admin account. The `cowrie` user cannot use sudo.
* **`192.168.1.165` does not respond while the VPN is on.** Use `10.0.0.1` through the tunnel instead.
* **Cowrie is logging but the dashboard is empty.** That is the log-serving HTTP server, not Cowrie. The first time this happened it was missing CORS headers.
