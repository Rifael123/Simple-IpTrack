import argparse
from colorama import Fore,Style
import time,os
import requests,json
import sys
import random
from time import sleep
from urllib import request
from sys import argv 

def berjalan(y):
  for x in y + "\n":
    sys.stdout.write(x)
    sys.stdout.flush()
    sleep(0.009)

print(Style.BRIGHT)

parser = argparse.ArgumentParser()
parser.add_argument( "-v ", help= "target/host IP adress", type=str, dest='target', required=True )
args = parser.parse_args()


berjalan(Fore.GREEN+"""


█████████████████████████████████████████
█▄─▄█▄─▄▄─█─▄─▄─█▄─▄▄▀██▀▄─██─▄▄▄─█▄─█─▄█
██─███─▄▄▄███─████─▄─▄██─▀─██─███▀██─▄▀██
▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀


""")

print("\n== IP Tracker - Rifael123 ==\n")
url = "http://ip-api.com/json/"
ip = args.target
request = request.urlopen(url + ip)
data_json = json.loads(request.read())

if data_json['status'] == "success":
	print(f"IP : {data_json['query']}")
	print(f"Country : {data_json['country']}")
	print(f"Region : {data_json['regionName']}")
	print(f"City : {data_json['city']}")
	print(f"Latitude : {data_json['lat']}")
	print(f"Longitude : {data_json['lon']}")
	print(f"ISP : {data_json['isp']}")
else:
	berjalan("Failed to find the IP informations.")
