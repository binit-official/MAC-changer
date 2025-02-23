#!/usr/bin/env python

import subprocess
import optparse
import re

def get_argumets():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address to change")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac address, use --help for more info")
    return options



def mac_change(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("Congratulation you have changed your Mac address for the interface "+interface)



def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    ifconfig_result_str = ifconfig_result.decode('utf-8')
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result_str)

    if mac_address_search_result:
        return (mac_address_search_result.group(0))
    else:
        print("[-] unable to read the mac value")


options=get_argumets()
current_mac=get_current_mac(options.interface)
print("current MAC = "+ str(current_mac))
mac_change(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to "+ current_mac)
else:
    print("[-] Unable to change the MAC address")



