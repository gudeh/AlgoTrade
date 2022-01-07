import requests
import pandas as pd
#from flask import Flask, request, render_template, session, redirect, make_response
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl import load_workbook
import time
from collections import ChainMap
import json
from Utils import config
from binance.spot import Spot as Client
import csv
import pprint
# import numpy as np
# app=Flask(__name__)

csv_name="out.csv"
def liveAction(one,two,three):
	with open(csv_name, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(["name,price,name,price,name,price,virutal,price,absolute difference, relative difference, percentage"])
	print("\t\t\t\t\t\t\t\t\t (virtual_third-third), [(virtual_third-third)/third], [1-(virtual_third/third)]\n",
		"\t\t\t\t\t\t\t\t\t (absolute difference), [relative difference], [percentage over original]")
	while True:
		r = requests.get("https://api.binance.com/api/v3/ticker/price")
		info = requests.get("https://api.binance.com/api/v3/exchangeInfo")
		info_json= info.json()
		infos_dict = {}
		for item in info_json['symbols']: #list of dicts
			name=item['symbol']
			status=item['status']
			permission=item['isSpotTradingAllowed']
			infos_dict[name]=[status,permission]

		ones_list= set()
		usdt_list= set()
		btc_list= set()
		price_json = r.json()
		prices_dict = {}
		for item in price_json:
			name = item['symbol']
			if name.find("USDT")!=-1:
				prices_dict[name] = float(item['price'])
				usdt_list.add(name.replace("USDT",""))
			if name.find("BTC")!=-1:
				prices_dict[name] = float(item['price'])
				btc_list.add(name.replace("BTC",""))
		ones_list=usdt_list.intersection(btc_list)
		# print(prices_dict)
		pair_two="BTCUSDT"
		real_two="BTCUSDT"
		invert2=False
		
		for one in ones_list:
		# if True == True:
		# 	one="PAX"
			pair_one=""
			pair_three=""
			invert1=invert3=False
			if one+two in prices_dict and two+one in prices_dict:
				pair_one=two+one
				real_one=two+one
			elif one+two in prices_dict:
				pair_one=one+two
				real_one=two+one
				invert1=True
				# print("A")
			elif two+one in prices_dict:
				pair_one=two+one
				real_one=two+one
				# print("B")
				
			else:
				print("FATAL! pair not found in both orders:",one,"+",two,"neither",two+one)

			if three+one in prices_dict and one+three in prices_dict:
				pair_three=one+three
				real_three=one+three
			elif three+one in prices_dict:
				pair_three=three+one
				real_three=one+three
				invert3=True
				# print("A")
			elif one+three in prices_dict:
				pair_three=one+three
				real_three=one+three
				# print("B")
				
			else:
				print("FATAL! pair not found in both orders:",three+one,"neither",one+three)
			first=0
			second=0
			third=0
			first=prices_dict[pair_one]
			if invert1:
				first=1/first
			second=prices_dict[pair_two]
			if invert2:
				second=1/second
			third=prices_dict[pair_three]
			if invert3:
				third=1/third

			virtual_third=(second/first)
			abs_diff=virtual_third-third
			relat_diff=(virtual_third-third)/third
			percentage=1-(virtual_third/third)


			if abs(relat_diff) > 0.1:
				if infos_dict[pair_one][0]=="TRADING" and infos_dict[pair_two][0]=="TRADING" and infos_dict[pair_three][0]=="TRADING":
					if infos_dict[pair_one][1] and infos_dict[pair_two][1] and infos_dict[pair_three][1]:
						print("got one:",pair_one,pair_two,pair_three,relat_diff)
						with open(csv_name, 'a', newline='') as csvfile:
							writer = csv.writer(csvfile, delimiter=',',
			                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
							writer.writerow([real_one,f"{first:.10f}",real_two,f"{second:.10f}",real_three,f"{third:.10f}",
								real_three+"virt",
								f"{virtual_third:6f}",
								f"{abs_diff:6f}",
								f"{relat_diff:6f}",
								f"{percentage:6f}"])
						
		time.sleep(1)
# 	print("PROCESSING HISTORICAL DATA")

if __name__ == "__main__":
	client = Client(config.API_KEY,config.API_SECRET)
	one="BRL"
	two="BTC"
	three="USDT"
	liveAction(one,two,three)
