#!/usr/bin/env python


import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    print('########################')
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    print('########################')
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    print('########################')


scan("10.0.2.1/24")
