from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router, Switch, VPN
from diagrams.generic.device import Mobile
from diagrams.generic.compute import Rack
from diagrams.generic.os import Windows
from diagrams.onprem.network import Internet

with Diagram("WireGuard VPN Server", filename="02-wireguard-topology", show=False, direction="TB"):
    with Cluster("Remote clients"):
        laptop = Windows("Windows laptop\n10.0.0.2")
        phone = Mobile("iPhone\n10.0.0.3")
    internet = Internet("Internet\nPublic IP (redacted)")
    with Cluster("Home network"):
        router = Router("Verizon CR1000A\nforward UDP 51820")
        with Cluster("Raspberry Pi 5 - 192.168.1.165"):
            wireguard = VPN("WireGuard wg0\n10.0.0.1")
            pihole = Rack("Pi-hole\nDNS filtering")
        lan = Switch("Home network\ninternal devices")
    [laptop, phone] >> Edge(label="encrypted tunnel") >> internet
    internet >> Edge(label="UDP 51820") >> router >> wireguard
    wireguard >> Edge(label="DNS") >> pihole
    wireguard >> lan
