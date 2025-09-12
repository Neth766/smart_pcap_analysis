"""
PacketProbe - Smart PCAP Analyzer
Author: Your Name

Description:
    A simple yet powerful PCAP analyzer built with Scapy.
    Shows protocol distribution, IP stats, top talkers, 
    and packet size details in a colorful, easy-to-read way.
"""

# ===================== IMPORTS =====================
# We try to import the modules we need.
# If some are missing, we will ask the user to install them.
import importlib
import sys
import subprocess
import os
from collections import Counter

# External libraries
try:
    from scapy.all import rdpcap, IP, TCP, UDP, ICMP
    from colorama import Fore, Style, init
except ImportError:
    print("\n[!] Required modules not found.")
    print("➡️  Please install them by running: pip install -r requirements.txt")
    sys.exit(1)

# Initialize colorama (for colorful text output on Windows/Linux)
init(autoreset=True)


# ===================== BANNER =====================
def show_banner():
    """Display a nice header when the program starts."""
    print(Fore.CYAN + "="*55)
    print(Fore.GREEN + "🔍 Welcome to " + Fore.YELLOW + "PacketProbe" + Fore.GREEN + " - Smart PCAP Analyzer")
    print(Fore.CYAN + "="*55 + "\n")


# ===================== MAIN ANALYZER =====================
def analyze_pcap(file_path):
    """
    Analyzes the given PCAP file and prints:
      - Total packets
      - Unique IPs
      - Protocol distribution
      - Top talkers (IP addresses sending most packets)
      - Packet size statistics
    """

    # Try to load the file
    try:
        packets = rdpcap(file_path)
    except FileNotFoundError:
        print(Fore.RED + f"[!] File not found: {file_path}")
        sys.exit(1)

    # Show basic file info
    print(Fore.CYAN + f"📂 File loaded: {file_path}")
    print(Fore.GREEN + f"[*] Total packets: {len(packets)}\n")

    # Counters for stats
    ip_counter = Counter()
    proto_counter = Counter()
    pkt_sizes = []

    # Process each packet
    for pkt in packets:
        pkt_sizes.append(len(pkt))  # Store packet size for later stats

        if IP in pkt:  # Only consider IP packets
            src = pkt[IP].src
            dst = pkt[IP].dst
            ip_counter[src] += 1
            ip_counter[dst] += 1

            # Count protocol usage
            if TCP in pkt:
                proto_counter["TCP"] += 1
            elif UDP in pkt:
                proto_counter["UDP"] += 1
            elif ICMP in pkt:
                proto_counter["ICMP"] += 1
            else:
                proto_counter["Other"] += 1

    # ===================== RESULTS =====================

    # Unique IP addresses
    unique_ips = list(ip_counter.keys())
    print(Fore.YELLOW + f"🌐 Unique IP addresses: {len(unique_ips)}")
    for ip in unique_ips[:10]:  # show only first 10 to keep output clean
        print(Fore.CYAN + f"   {ip}")

    # Protocol distribution
    print(Fore.YELLOW + "\n📊 Protocol distribution:")
    for proto, count in proto_counter.items():
        print(Fore.CYAN + f"   {proto}: {count}")

    # Top 5 talkers (IPs that appear most often)
    print(Fore.YELLOW + "\n💬 Top 5 Talkers (most packets):")
    for ip, count in ip_counter.most_common(5):
        print(Fore.CYAN + f"   {ip} -> {count} packets")

    # Packet size statistics
    if pkt_sizes:
        avg_size = sum(pkt_sizes) / len(pkt_sizes)
        print(Fore.YELLOW + "\n📏 Packet size stats:")
        print(Fore.CYAN + f"   Smallest: {min(pkt_sizes)} bytes")
        print(Fore.CYAN + f"   Largest : {max(pkt_sizes)} bytes")
        print(Fore.CYAN + f"   Average : {avg_size:.2f} bytes")

    print(Fore.GREEN + "\n✅ Analysis complete! Thanks for using PacketProbe 🚀")


# ===================== MAIN ENTRY =====================
if __name__ == "__main__":
    show_banner()

    # If user gives a file path as argument, use that.
    # Otherwise, fall back to "ipv4frags.pcap" in the same folder as the script.
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = os.path.join(os.path.dirname(__file__), "ipv4frags.pcap")

    analyze_pcap(file_path)
