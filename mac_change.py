# Code to change MAC address in KALI LINUX

import subprocess as sp
import optparse as op
import random
import re


def rand_mac():
    mac = [ 0x00, 0x16, 0x3e,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def change_mac(interface, new_mac):
    mac = get_output(interface)
    if mac:
        sp.call(['sudo', 'ifconfig', interface, 'down'])
        sp.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
        sp.call(['sudo', 'ifconfig', interface, 'up'])
        mac = get_output(interface).decode()
        print("Your new MAC address is " +mac)
    else:
        exit()
  

def get_args():
    parser = op.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help="[Interface to change its MAC address. ]")
    parser.add_option('-m', '--mac', dest='new_mac', help="[New MAC address you want to assign.  ]")
    option,arguments = parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an interface, use --help for more information.")
        exit()
    if not option.new_mac:
        change_mac(option.interface,rand_mac())
        exit()
    else:
        return parser.parse_args()


def get_output(interface):
    return sp.check_output('cat /sys/class/net/'+interface+'/address', shell=True)
    

option,argument = get_args()
change_mac(option.interface, option.new_mac)
