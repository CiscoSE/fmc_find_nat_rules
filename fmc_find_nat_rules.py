#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FMC_Find_NAT_Rules Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Niranjan Kiran Kumar Dhurjaty"
__email__ = "nidhurja@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


#
# Generated FMC REST API sample script
# This Script is only to search through NAT rules for given IP ADDRESS.
# Multi Domain is not considered on this script. Please use the domain id field for the same.
#

import json
import sys
import requests
import argparse

from urllib3.exceptions import InsecureRequestWarning


############################################################################################
#                                                                                          #
# Pull all NAT rules in a NAT policy and match the object ID with the ID LIST prepared     #
# Based on the IP Address for search                                                       #
############################################################################################


def Find_n_Match_NatRule(objectid,PolicyName):
  global ObjtoFind

  api_path = "/policy/ftdnatpolicies/"  + objectid + "/natrules?expanded=true&limit=1000"
  url = server + api_path_fixed + DomainUUID + api_path
  if (url[-1] == '/'):
      url = url[:-1]
  try:
    s = requests.get(url, headers=headers, verify=False)
    status_code = s.status_code
    resp = s.text
    if (status_code == 200):
       print("\n\nGET successful for NAT Policy --> " + PolicyName + "\n")
       json_resp_local = json.loads(resp)
       RuleNumber = 1
       if ( json_resp_local['paging']['count'] == 0):
           print("No matching Rules in this Policy\n\n")
           if s : s.close()
       else:
           for j in json_resp_local['items']:
              if (j['type'] == 'FTDManualNatRule'):
                for a in NetworkObjList:
                  if (a['Obj'] == j['originalSource']['id']):
                    print(" \n\n NAT Rule Match at line number " + str(RuleNumber) + "\n\n")
                    print(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')))
              else:
                for a in NetworkObjList:
                  if (a['Obj'] == j['originalNetwork']['id']):
                    print(" \n\n NAT Rule Match at line number " + str(RuleNumber) + "\n\n")
                    print(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')))

              RuleNumber = RuleNumber + 1
    else:
       s.raise_for_status()
       print("Error occurred in GET --> "+resp)
  except requests.exceptions.HTTPError as err:
    print ("Error in connection --> "+str(err))
  finally:
   if s : s.close()

   ############################################################################################
   #                                                                                          #
   # Prepare a list of network objects and groups matching the IP ADDRESS in the arguments    #
   #                                                                                          #
   ############################################################################################

def FindNetworkObj(api_path):
  global ObjtoFind
  global NetworkObjList

  try:
       r = requests.get(url, headers=headers, verify=False)
       status_code = r.status_code
       resp = r.text
       if (status_code == 200):
          print("\n\nGET successful. Loading Newwork Objects --> \n\n")
          json_resp = json.loads(resp)
          for i in json_resp['items']:

            if IPAddToFind == i['value']:
              NetworkObj['name']= i['name']
              NetworkObj['Obj']= i['id']
              ObjtoFind = NetworkObj
              NetworkObjList.append(NetworkObj.copy())
       else:
          r.raise_for_status()
          print("Error occurred in GET --> "+resp)
  except requests.exceptions.HTTPError as err:
       print ("Error in connection --> "+str(err))
  finally:
      if r : r.close()

      ############################################################################################
      #                                                                                          #
      # Prepare a list of network groups matching the IP ADDRESS in the arguments                #
      #                                                                                          #
      ############################################################################################
def FindNetworkGrp(api_path):
      global ObjtoFind
      global NetworkObjList
      #global NameToFind

      try:
          r = requests.get(url, headers=headers, verify=False)
          status_code = r.status_code
          resp = r.text
          if (status_code == 200):
             print("\n\nGET successful. Loading Newwork Groups --> \n\n")
             json_resp = json.loads(resp)
             for i in json_resp['items']:
               if (NameToFind == i['name']):
                 print (i['name'])
                 NetworkObj['name']= i['name']
                 NetworkObj['Obj']= i['id']
                 ObjtoFind = NetworkObj
                 NetworkObjList.append(NetworkObj.copy())
          else:
             r.raise_for_status()
             print("Error occurred in GET --> "+resp)
      except requests.exceptions.HTTPError as err:
          print ("Error in connection --> "+str(err))
      finally:
        if r : r.close()

      ############################################################################################
      #                                                                                          #
      # Main Code Starts Here. Execution starts here.                                            #
      #                                                                                          #
      ############################################################################################

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
server = ""
NetworkObjList = [{'name':'none','Obj':'None'}]
NetworkObj= {'name':'none','Obj':'None'}
ObjtoFind = {'name':'none','Obj':'None'}
api_path_fixed ="/api/fmc_config/v1/domain/"

count = 1



parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("FMCIP",help="IP Address / Hostname of FMC, Please do not add any suffix like-Https:")
parser.add_argument("username", help="Username of FMC")
parser.add_argument("password", help="password of FMC")
parser.add_argument("Switch", help= "'i' for searching with IP Address or 'g' for Group",choices=['i','g'])
parser.add_argument("IPorGroup", help="IP Address / Group to filter the NAT rules")

args = parser.parse_args()
server= "https://" + args.FMCIP
username = args.username
password = args.password
WhatToFind= args.Switch
if (WhatToFind == 'g'):
  NameToFind = args.IPorGroup
else:
  if (WhatToFind == 'i'):
    IPAddToFind = args.IPorGroup  

print ("\n Generating Token and Connecting \n\n")
r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path
try:
      r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
      auth_headers = r.headers
      auth_token = auth_headers.get('X-auth-access-token', default=None)
      if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print ("Error in generating auth token --> "+str(err))
    sys.exit()

headers['X-auth-access-token']=auth_token
print ("\nConnected Successfully \n")
DomainUUID=auth_headers['DOMAIN_UUID']
print ("\n\nDomain UUID IS: " + DomainUUID) # Check for the Domain Id and replace the URLs.
if (WhatToFind=='i'):
  api_path = "/object/networkaddresses?expanded=True&limit=1000"
  url = server + api_path_fixed + DomainUUID + api_path
  if (url[-1] == '/'):
    url = url[:-1]
  FindNetworkObj(api_path)
else:
  if (WhatToFind == 'o'):
    api_path = "/object/networkgroups?expanded=True&limit=1000"
    url = server + api_path_fixed + DomainUUID + api_path
    if (url[-1] == '/'):
      url = url[:-1]
    FindNetworkGrp(api_path)
  else:
    sys.exit()

api_path = "/policy/ftdnatpolicies?expanded=True&limit=1000"
url = server + api_path_fixed + DomainUUID + api_path
if (url[-1] == '/'):
    url = url[:-1]
try:
     r = requests.get(url, headers=headers, verify=False)
     status_code = r.status_code
     resp = r.text
     if (status_code == 200):
         print("GET successful. Response data --> ")
         json_resp = json.loads(resp)
         for i in json_resp['items']:
             Find_n_Match_NatRule ( i['id'],i['name'])

     else:
         r.raise_for_status()
         print("Error occurred in GET --> "+resp)
except requests.exceptions.HTTPError as err:
     print ("Error in connection --> "+str(err))
finally:
     if r : r.close()
