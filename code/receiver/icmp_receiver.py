from scapy.all import sniff, IP, ICMP

def handle_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(ICMP):
        if packet[ICMP].type == 8:
            packet.show()

sniff(filter="icmp", prn=handle_packet)
