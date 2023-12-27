#!/usr/bin/python3

import dns.resolver
import argparse
import sys
from colorama import Fore

if "--entrytype-list" in sys.argv:
    print("A \t= IPv4 format\nAAAA \t= Ipv6 format\nMX \t= Mail Servers\nTXT \t= Text entries\nNS \t= Nameservers\nANY \t= All above")
    exit()

parser = argparse.ArgumentParser(description="DNS Resolver tool.")

parser.add_argument('-H','--hostname',required=False)
parser.add_argument('-T','--entrytype',required=True,help='See more --entrytype-list')
parser.add_argument('-F','--file',required=False,help='File to various hosts')

args = parser.parse_args()

hostname = args.hostname
entrytype = args.entrytype
file = args.file

resolver = dns.resolver.Resolver()

hosts = []

if args.file != None and args.hostname == None:
    try:
        with open(file, 'r') as f:
            for i in f:
                hosts.append(i.strip())
    except FileNotFoundError as error:
        print(Fore.RED + "\n[!] File not found!")

elif args.hostname != None and args.file == None:
    hosts.append(args.hostname)

else:
    print(Fore.RED + "Select between one host (-H) or more with file (-F)")
    exit()

print("")

try:
    for host in hosts:
        print(Fore.CYAN + f"\n[*] TARGET: {host}")
        result = resolver.resolve(host,entrytype)
        output = []
        for i in result:
                output.append(i)
        if entrytype == "A":
            print(Fore.YELLOW + f"[!] IPv4 Servers Encountered:")
            for i in output:
                print(Fore.GREEN + f"[+] {i}")
        elif entrytype == "AAAA":
            print(Fore.YELLOW + f"[!] IPv6 Servers Encountered:")
            for i in output:
                print(Fore.GREEN + f"[+] {i}")
        elif entrytype == "MX":
            print(Fore.YELLOW + f"[!] MAIL Servers Encountered:")
            for i in output:
                print(Fore.GREEN + f"[+] {i}")
        elif entrytype == "TXT":
            print(Fore.YELLOW + f"[!] TXT Entries Encountered:")
            for i in output:
                print(Fore.GREEN + f"[+] {i}")
        elif entrytype == "NS":
            print(Fore.YELLOW + f"[!] NAME Servers Encountered:")
            for i in output:
                print(Fore.GREEN + f"[+] {i}")

except Exception as error:
    print(Fore.RED + f"{error}")
