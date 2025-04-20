#  ARP Spoof Tool

This Python script performs ARP spoofing attacks to poison the ARP cache of a target and the gateway, enabling a Man-in-the-Middle (MITM) attack.

##  Features
- Retrieves MAC addresses using ARP requests.
- Sends spoofed ARP responses to target and gateway.
- Restores ARP tables upon termination.

## Usage
```bash
sudo python arp_spoof.py -t <target_ip> -g <gateway_ip>
```

## Requirements
- Python 3.x
- `scapy`
- `termcolor`
- Root privileges

## Disclaimer
This tool is for educational purposes only. Do not use it on unauthorized networks.