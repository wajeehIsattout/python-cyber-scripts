# Python Backdoor Client

This script is a Python-based backdoor client that connects to a listener on Kali Linux and provides shell access, file upload/download, and directory navigation.

## Features
- Reliable JSON-based communication
- Remote shell execution
- File upload/download (Base64)
- Change working directory

## Usage
1. Run the listener (custom or Netcat) on your Kali VM:
```bash
nc -lvp 4444
```

2. On the target, run the backdoor script:
```bash
python backdoor_client.py
```

**Default target IP and port:** `192.168.56.129:4444` (edit as needed in the script)

## Requirements
- Python 3.x

## Disclaimer
For educational and authorized penetration testing only. Do not deploy on unauthorized systems.