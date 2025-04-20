# Basic Web Crawler Scanner

## Description
This script is a basic web crawler that recursively scans all internal links within a specified target URL. It uses a session to maintain state (like login sessions) and extracts links using regular expressions.

## Features
- Crawls through all internal links starting from the target URL
- Maintains session for authenticated scanning
- Skips duplicate links and fragments

## Requirements
- Python 3
- `requests` library

## Usage
```bash
python Crawler.py
```

Make sure to replace the `target_url` and login `data_dict` with your own credentials.

## Disclaimer
Use this script only on systems you have permission to test.
