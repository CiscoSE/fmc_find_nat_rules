
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/CiscoSE/fmc_find_nat_rules)

# FMC_Find_NAT_Ruls.py

*Finds the NAT Rules by IP Address or Network Groups*

---

## Motivation
Currently there is no option available in FMC for searching the NAT Rules. So administrator has to go every NAT rule to find the specific rule. In complex environments it might be difficult to find the same especially in troubleshooting sessions. This scripts saves the time by searching the NAT Rules.




# A tutorial of argparse! .
------------------------------------------------------------------------------------------------


fmc_find_nat_rules nidhurja$ python3 fmc_find_nat_rules.py -h

usage: fmc_find_nat_rules.py [-h] FMCIP username password {i,g} IPorGroup

A tutorial of argparse!

positional arguments:

  FMCIP       IP Address / Hostname of FMC, Please do not add any suffix like-
              Https:
              
  username    Username of FMC
  
  password    password of FMC
  
  {i,g}			i or g
  
  IPorGroup   IP Address / Group to filter the NAT rules

optional arguments:
  -h, --help  show this help message and exit
  
NIDHURJA-M-433C:fmc_find_nat_rules nidhurja$ 


-----------------------------------------------------------------------------------------------------

# Features

Search can be based on the IP Address or Network Group.

The search parameter is considered as Original Source / source Group in FMC NAT rules and Original network in the Auto NAT rules.

Scripts considers all instances of IP Addresses and Groups while searching the NAT Rules and displays. 

All NAT policies are searched for individual NAT Rules for the match. If Match is found scripts returns the line number and NAT Rule as well.

Script is written and tested for single domain deployment of FMC.


# Technologies & Frameworks Used
FMC APIs are used.

NO Third-Party products or Services are used.

Script is written in Python 3

# Installation
1, Create an empty directory

2, cd into it and <git clone https://github.com/CiscoSE/fmc_find_nat_rules.git>, as this will work only in empty directories

3, create the virtual environment in a subdir in the same directory

4, Start the VE and install requirements.txt from the <fmc_find_nat_rules>

Execute the script as any other Python script form console. Check the reachability to FMC. Script is tested on FMC 6.3.



# Authors & Maintainers

This is my first script in PYthon, contact me for any modifications on this script.

Niranjan Kiran Kumar Dhurjaty nidhurja@cisco.com

# Extensions
Script can be extended in the following ways.
Search can be restricted to first 3 octets of IPv4 address, so that user may get more flexibility.
Search and list all groups with IP address provided in switch “I”. This will eliminate the requirement of “ Group name search ”.
# License
This project is licensed to you under the terms of the Cisco Sample
Code License.