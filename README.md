# raspberry-pi-home-lab
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%205-red)
![License](https://img.shields.io/badge/License-MIT-blue)


## Cybersecurity & Networking Home Lab

This repository documents my personal cybersecurity and networking home lab built around a Raspberry Pi 5, my home network, and a Windows laptop. I am using this lab to build real hands-on skills for a future role in cybersecurity, networking, SOC analysis, or IT infrastructure.

The goal is not just to install tools, but to understand how they work, document the process, take screenshots, break things, fix them, and explain everything clearly like I would in a real technical environment.

---

## Lab Overview

Current lab setup:

```text
                 Internet
                    |
                    v
        Verizon CR1000A Router
                    |
                    v
   Raspberry Pi 5 - Pi-hole DHCP + DNS
                    |
        -------------------------
        |          |            |
        v          v            v
   Windows      Phone        Smart TV
   Laptop       Devices      Other Devices
```

Right now, the Raspberry Pi 5 is running Pi-hole as the main DNS and DHCP server for the home network. All home devices receive network settings from the Pi and use it for DNS filtering.

This gives me a real environment to practice DNS, DHCP, Linux administration, router configuration, logging, troubleshooting, and network security basics.

---

## Projects

| Status     | Project                           | Description                                                          | Key Tools                                        | Link                                     |
| ---------- | --------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| ✅ Done     | 01 - Pi-hole DNS Sinkhole         | Network-wide DNS filtering and DHCP setup using Raspberry Pi 5       | Pi-hole, Raspberry Pi OS, Linux, Verizon CR1000A | [View Project](./01-pihole-dns-sinkhole) |
| 🔜 Planned | 02 - WireGuard VPN Server         | Secure remote access into the home lab network                       | WireGuard, Linux, UDP, Port Forwarding           | Coming soon                              |
| 🔜 Planned | 03 - Honeypot with Cowrie         | SSH honeypot to study attacker behavior and collect logs safely      | Cowrie, Python, SSH, Linux Logs                  | Coming soon                              |
| 🔜 Planned | 04 - IDS with Suricata            | Intrusion detection system for monitoring suspicious network traffic | Suricata, PCAP, Rules, Alerts                    | Coming soon                              |
| 🔜 Planned | 05 - Centralized SIEM             | Central log collection and dashboarding for lab security events      | ELK Stack, Elasticsearch, Logstash, Kibana       | Coming soon                              |
| 🔜 Planned | 06 - Active Directory Lab         | Windows domain lab for learning enterprise identity and security     | Windows Server, AD DS, DNS, Group Policy         | Coming soon                              |
| 🔜 Planned | 07 - Network Monitoring with Zeek | Network traffic analysis and protocol logging                        | Zeek, Linux, Network Logs                        | Coming soon                              |

---

## Skills I Am Building

* Linux command line administration
* DNS and DHCP configuration
* Home router and LAN troubleshooting
* Raspberry Pi server management
* Network security fundamentals
* Log collection and analysis
* Firewall and port forwarding concepts
* VPN setup and secure remote access
* Intrusion detection basics
* SIEM dashboards and alerting
* Documentation and GitHub project organization
* Real-world troubleshooting mindset

---

## Tools & Technologies

![Raspberry Pi](https://img.shields.io/badge/-Raspberry%20Pi-C51A4A?style=flat&logo=Raspberry-Pi)
![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Pi-hole](https://img.shields.io/badge/-Pi--hole-96060C?style=flat&logo=pi-hole&logoColor=white)
![WireGuard](https://img.shields.io/badge/-WireGuard-88171A?style=flat&logo=wireguard)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)

## Current Project: Pi-hole DNS Sinkhole

The first completed project is a Pi-hole DNS sinkhole running on my Raspberry Pi 5.

What I completed:

* Installed Raspberry Pi OS
* Connected to the Pi using SSH
* Installed Pi-hole
* Configured Pi-hole as the DNS server
* Moved DHCP from the Verizon CR1000A router to Pi-hole
* Verified that home devices receive IP addresses from Pi-hole
* Tested DNS blocking across the network
* Accessed and reviewed the Pi-hole admin dashboard
* Documented issues and fixes during setup

This project helped me understand how DNS requests move through a home network and how DNS filtering can block ads, trackers, and unwanted domains before traffic reaches the device.

---

## Why I Am Building This Lab

I am learning cybersecurity and networking by building instead of only watching videos or reading notes. Every project in this repository is meant to help me practice real skills that are useful in IT and cybersecurity jobs.

This lab gives me a place to make mistakes, troubleshoot problems, and slowly build confidence with tools that are used in real environments.

I want this repository to show my progress over time, from basic networking projects to more advanced security monitoring, logging, honeypots, VPNs, and enterprise-style labs.

---

## Repository Structure

```text
raspberry-pi-home-lab/
│
├── 01-pihole-dns-sinkhole/
│   ├── README.md
│   ├── screenshots/
│   └── notes.md
│
├── 02-wireguard-vpn-server/
│   └── README.md
│
├── 03-cowrie-honeypot/
│   └── README.md
│
├── 04-suricata-ids/
│   └── README.md
│
├── 05-elk-siem/
│   └── README.md
│
├── 06-active-directory-lab/
│   └── README.md
│
├── 07-zeek-network-monitoring/
│   └── README.md
│
└── README.md
```

---

## Documentation Style

Each project will include:

* Project goal
* Network diagram when needed
* Hardware and software used
* Step-by-step setup process
* Screenshots
* Problems I ran into
* How I fixed them
* What I learned
* Possible improvements

I want the documentation to be clear enough that someone else could follow it, but also honest enough to show the actual learning process.

---

## Lab Hardware

| Item                   | Use                                                     |
| ---------------------- | ------------------------------------------------------- |
| Raspberry Pi 5         | Main home lab server                                    |
| Verizon CR1000A Router | Home internet router                                    |
| Windows Laptop         | Management, testing, SSH, GitHub documentation          |
| Home Devices           | Real clients for testing DNS, DHCP, and network changes |

---

## Long-Term Goal

The long-term goal is to turn this into a complete beginner-to-intermediate cybersecurity home lab that shows growth across networking, Linux, detection engineering, log analysis, and security operations.

This repository will keep growing as I build more projects and improve the lab.

---

## License

This project is licensed under the MIT License.

---

## Author

Built and documented by Maankumar Patel, cybersecurity and networking student.
