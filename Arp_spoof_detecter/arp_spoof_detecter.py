#!/usr/bin/env python
import scapy.all as scapy
from termcolor import colored
import optparse
import sys

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest ="interface", help="the interface")
    (options, arguments) = parser.parse_args()
    return options


def sniff(interface):
    try:
        scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)
    except KeyboardInterrupt:
        print("\n[+] Detected Ctrl+C... Exiting now.")
        sys.exit()


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op==2:
        try:
            real_mac=get_mac(packet[scapy.ARP].psrc)
            response_mac=packet[scapy.ARP].hwsrc
            if real_mac and real_mac != response_mac:
                print(colored("[+] YOU ARE UNDER ATTACK!!", 'red'))
            elif not real_mac:
                print(colored("Could not determine the real MAC address.", 'yellow'))

        except IndexError:
            pass
        except KeyboardInterrupt:
            print("\n[+] Detected Ctrl+C... Exiting now.")
            sys.exit()





def get_mac(ip, timeout=1):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=timeout, verbose=False)[0]
        if answered_list:
           return answered_list[0][1].hwsrc
        else:
            return None
    except KeyboardInterrupt:
        print("\n[+] Detected Ctrl+C... Exiting now.")
        sys.exit()


options=get_arguments()
interface_to_use=options.interface
sniff(interface_to_use)