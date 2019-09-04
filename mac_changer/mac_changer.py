#!/usr/bin/env python
import subprocess
from optparse import OptionParser

def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (options,args) = parser.parse_args()
    if not options.interface:
        print ("[-] Please provide an interface, use --help for more info.")
        exit()
    elif not options.new_mac:
        print ("[-] Please provide a new_mac, use --help for more info.")
        exit()
    return options

def mac_changer(interface,new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
mac_changer(options.interface,options.new_mac)
