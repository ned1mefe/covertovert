from scapy.all import IP, ICMP, send

packet = IP(dst="receiver", ttl=1) / ICMP()

send(packet)
