# Network-Config-and-Sockets
Computer Networks projects (Spring 2024): WAN setup with Cisco Packet Tracer &amp; TCP/UDP socket programming

## Table of Contents
- [Project 1: Wide Area Network Setup](#project-1-wide-area-network-setup)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Lab Tasks](#lab-tasks)
  - [Deliverables](#deliverables)
- [Project 2: Socket Programming](#project-2-socket-programming)
  - [Overview](#overview-1)
  - [Implementation Details](#implementation-details)
  - [Deliverables](#deliverables-1)
  - [How to Run](#how-to-run)

---

## Project 1: Wide Area Network Setup

### Overview

This project involves designing and configuring a Wide Area Network (WAN) for a mock bank branch. The setup includes:

- Three LANs (one with two VLANs)
- Cisco routers and switches
- IP addressing, VLANs, Inter-VLAN routing, static routing, and SSH security configuration

### Requirements

- **Software:** Cisco Packet Tracer 8.2.1 or later
- **Skills Required:** Networking concepts, Cisco IOS configuration, subnetting, VLANs, routing

### Lab Tasks

1. **IP Addressing Scheme:** Subnet the 172.16.10.0/16 network into seven subnets.
2. **VLANs & Trunking:** Create VLANs (Management, Marketing, Accounting) and configure access/trunk ports.
3. **IP Address Assignment:** Assign subnets and IPs to network devices.
4. **Inter-VLAN Routing:** Configure router sub-interfaces for VLAN communication.
5. **Static Routing:** Set up static routes and default routes.
6. **Security Settings:** Secure routers and switches with user accounts, encrypted passwords, and SSH access.
7. **Testing & Troubleshooting:** Verify configurations with `ping`, `show` commands, and troubleshooting steps.

### Deliverables

- **Packet Tracer File:** Complete network topology with saved configurations.
- **Documentation:** Addressing table, configuration steps, and screenshots.

---

## Project 2: Socket Programming

### Overview

Develop a client-server application using sockets in **Python, C/C++, or Java**. The project consists of two implementations:
1. **TCP Socket Server**: Receives strings from clients and returns the reversed string.
2. **UDP Socket Server**: Same functionality but using UDP.

### Implementation Details

- The server should handle at least **5 simultaneous clients**.
- Clients can send multiple strings, and the server should respond accordingly.
- Both client and server should display sent/received messages.
- The server must run on a separate machine from the clients.

### Deliverables

- **Source Code**: Well-commented code for both TCP and UDP implementations.
- **Design Document**: Overview of program architecture, design decisions, and improvements.
- **Testing Report**: Description of test cases, execution traces, and known limitations.
- **Build & Execution Guide**: Instructions on compiling and running the program.

### How to Run

#### TCP Server & Client

```sh
# Run the server
python tcp_server.py

# Run a client
python tcp_client.py
```

#### UDP Server & Client

```sh
# Run the server
python udp_server.py

# Run a client
python udp_client.py
```

For multiple clients, open separate terminals and execute the client script multiple times.

---

## Contributors

- **Instructor:** Prof. Yahya Z. Mohasseb
- **Assistant:** Eng. Nourhan Tarek
- **Course:** CC431 - Computer Networks
- **Team Members:** Anton Ashraf, Abdelmalek Osama, Nouran Mostafa, Lina Wael

---

## License

This project is for academic purposes and follows open-source principles. Feel free to modify and enhance it!
