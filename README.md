# Network Forensics CLI

The Network Forensics CLI is a Python-based command-line interface for analyzing network traffic captured in pcap files. With this tool, you can dynamically interact with captured packets, apply filters, and perform various analyses. The CLI provides an intuitive interface to explore and extract information from network packets, making it a valuable asset for network security and forensics tasks.

## Key Features

- Extract and display packet information including source, destination, protocol, and timestamp.
- Apply filters to focus on specific types of packets (e.g., TCP, UDP) or based on IP addresses.
- Identify potential large data transfers during packet analysis.
- Perform dynamic analysis and gain insights into network activities.

## Requirements

- Python 3.x
- PyShark library
- Click library

## Installation

- pip install pyshark click

## Usage

1. Clone the repository.
2. Run the CLI with a pcap file as an argument.
3. Interact with the CLI to explore and analyze network packets.

## Dependencies

- [PyShark](https://github.com/phaethon/pyshark)

## Getting Started

```bash
# Clone the repository
git clone https://github.com/BHK0407/network_forensics-cli.git

# Change to the project directory
cd network-forensics-cli

# Run the CLI with a pcap file
python3 network_forensics.py /path/to/your/capture_file.pcap

Explore the world of network forensics and enhance your ability to investigate and understand network traffic patterns.

## Lincense

This project is licensed under the MIT License.





