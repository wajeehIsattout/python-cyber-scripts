# ARP Spoof Detector

A tool to detect ARP spoofing attempts in real time by comparing the real MAC address of IPs against observed ARP replies.

## Features
- Sniffs ARP packets using `scapy`.
- Compares response MAC with actual MAC.
- Alerts if spoofing is detected.

## Usage
```bash
sudo python arp_spoof_detector.py -i <interface>
```

## Requirements
- Python 3.x
- `scapy`
- `termcolor`

## ⚠️ Disclaimer
Use in authorized environments only for network monitoring and educational purposes.