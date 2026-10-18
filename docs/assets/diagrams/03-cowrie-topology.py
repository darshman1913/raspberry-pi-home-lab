from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router
from diagrams.generic.compute import Rack
from diagrams.generic.device import Tablet
from diagrams.generic.storage import Storage
from diagrams.onprem.network import Internet

with Diagram("Cowrie SSH Honeypot", filename="03-cowrie-topology", show=False, direction="TB"):
    internet = Internet("Internet\nattackers and scanners")
    with Cluster("Home network"):
        router = Router("Verizon CR1000A\nTCP 22 -> 2222")
        with Cluster("Raspberry Pi 5"):
            cowrie = Rack("Cowrie honeypot\nhostname: ubuntu-server\nport 2222")
            json_logs = Storage("JSON logs")
            text_logs = Storage("Text logs")
    dashboard = Tablet("Custom dashboard\nHTML/JavaScript")
    internet >> Edge(label="port 22") >> router >> cowrie
    cowrie >> [json_logs, text_logs]
    json_logs >> dashboard
