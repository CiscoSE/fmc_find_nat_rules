# FMC_Find_NAT_Ruls.py

*Finds the NAT Rules by IP Address or Network Groups*

---

## Motivation
As of now ther is no option avialable on FMC for searching the NAT Rules. So Admin has to go page by page to search the rule. In complex environments it might be difficult to find the same. This scripts saves the time by searching the NAT Rules.

## Show Me!

Sample use of script with output.
------------------------------------------------------------------------------------------------
Python3 fmc_find_nat_rules.py FMC_IPAddress usename password i IPAddress

Connected Successfully 

Domain UUID IS: e276abec-e0f2-11e3-8169-6d9ed49b625f

GET successful. Loading Network Objects --> 

GET successful. Response data --> 

GET successful for NAT Policy --> FTD-Mig-1554755781
 

 NAT Rule Match at line number 16

{
    "destinationInterface": {
        "id": "SampleCodeGrp",
        "type": "InterfaceGroup"
    },
    "dns": false,

-----------------------------------------------------------------------------------------------------

## Features

- Search can be based on the IP Address or Network Group.
- The search paremeter is considered as Original Source / source Group in FTD NAT rules and Original network in the Auto NAT rules.
- Scripts considers all instances of IP Addresses and Groups while searching the NAT Rules. In FMC Multiple Network Objects can be created with the    same IP Address and same Network Object can be used in Multiple Network Groups.
- All NAT plocicies are searched for individual NAT Rules for the match. If Match is found scripts returns the line number and NAT Rule as well. 
- Script is written and tested for single domain deployment of FMC.

## Technologies & Frameworks Used

- FMC APIs are used.

- NO Third-Party products or Services are used.

- Script is written in Python 3

## Usage
Script will take 5 parameters. 

1. IPAddressofFMC - IP Address of FMC device. 
2. Username - username of FMC
3. Password - Password of FMC
4. switch g/i - If user wants to search with IP Address use "i" as a switch.
                If user wants to search with Network Group use "g" switch.

5. Name/IP address - Name of the Netwrok group or IP Address to search the NAT rules.

## Installation

Execute the script as any other Python script form console. Check the reachbility to FMC. Script is tested on FMC 6.3.

## Authors & Maintainers

This is my first script in PYthon, contact me for any modifications on this script.

- Niranjan Kiran Kumar Dhurjaty <nidhurja@cisco.com>

## Extensions

- Script can be extended in the following ways.
- Search can be restricted to first 3 octets of IPv4 address, so that user may get more flexibility.
- Search and list all groups with IP address provided in switch “I”. This will eliminate the requirement of “Group name search”.

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).


