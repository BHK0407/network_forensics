import click
import pyshark

# Global variable for the pcap file and the packet filter
pcap_file = None
packet_filter = lambda packet: True

def extract_information(packet):
    # Extract and print relevant information
    if hasattr(packet, 'ip'):
        click.echo(f"Source: {packet.ip.src}")
        click.echo(f"Destination: {packet.ip.dst}")
        click.echo(f"Protocol: {packet.transport_layer}")
        click.echo(f"Timestamp: {packet.sniff_timestamp}")
        click.echo("\n")
    else:
        click.echo("Packet does not have an IP layer\n")

def analyze_traffic(packet):
    # Check for large data transfers
    if hasattr(packet, "length") and int(packet.length) > 1000:
        click.echo("Potential large data transfer detected!")
        click.echo("\n")


def analyze_pcap(file_path, packet_filter):
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        if packet_filter(packet):
            extract_information(packet)
            analyze_traffic(packet)


@click.command()
@click.argument("file_path", type=click.Path(exists=True))

def cli(file_path):
    global pcap_file
    pcap_file = file_path

    click.echo("Welcome tho the Network Forensics CLI!")
    run_interactive_mode()


def run_interactive_mode():
    global packet_filter
    while True:
        click.echo("\nOptions:")
        click.echo("1. Display all packets")
        click.echo("2. Filter by TCP")
        click.echo("3. Filter by UDP")
        click.echo("4. Filter by IP address")
        click.echo("5. Run analysis")
        click.echo("0. Exit")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 0:
            click.echo("Thank you, Goodbye!")
            break
        elif choice == 1:
            packet_filter = lambda packet: True
        elif choice == 2:
            packet_filter = lambda packet: hasattr(packet, 'ip') and packet.transport_layer == 'TCP'
        elif choice == 3:
            packet_filter = lambda packet: hasattr(packet, 'ip') and packet.transport_layer == 'UDP'
        elif choice == 4:
            ip_address = click.prompt("Enter IP address to filter")
            packet_filter = lambda packet: hasattr(packet, 'ip') and (packet.ip.src == ip_address or packet.ip.dst == ip_address)
        elif choice == 5:
            if pcap_file is not None:
                click.echo("Running analysis...")
                analyze_pcap(pcap_file, packet_filter)
            else:
                click.echo("Please provide a valid pcap file.")
        else:
            click.echo("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli()
