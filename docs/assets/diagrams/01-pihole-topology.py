from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router, Switch
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.compute import Rack
from diagrams.onprem.network import Internet

with Diagram("Pi-hole DNS Sinkhole", filename="01-pihole-topology", show=False, direction="TB"):
    internet = Internet("Internet")
    with Cluster("Home network"):
        router = Router("Verizon CR1000A\nDHCP disabled")
        with Cluster("Raspberry Pi 5"):
            pihole = Rack("Pi-hole\nDNS + DHCP\n192.168.1.165")
        clients = [Switch("LAN"), Mobile("Phones"), Tablet("Smart TV")]
    internet >> Edge(label="upstream 1.1.1.1") >> pihole
    router >> pihole >> clients
