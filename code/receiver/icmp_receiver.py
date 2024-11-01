from scapy.all import sniff, IP, ICMP

def handle_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(ICMP):
        if packet[ICMP].type == 8:
            packet.show()

if __name__ == "__main__":
    sniff(filter="icmp", prn=handle_packet)
