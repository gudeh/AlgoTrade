import time as t
import pandas as pd
import numpy as np
from Utils import mytest_ubuntu
import requests
import pprint
pp = pprint.PrettyPrinter(width=10,indent=5,depth=3)
from binance.spot import Spot as Client #REST option
from datetime import datetime
import matplotlib.pyplot as plt
from PricePrediction.myUtils import *

fake_client = Client(base_url="https://testnet.binance.vision")
key = mytest_ubuntu.API_KEY
secret = mytest_ubuntu.API_SECRET
spot_client = Client(key, secret, base_url="https://testnet.binance.vision")

mysymbol="BTCBUSD"
all_intervals=["1m","5m","1h","2h"]
all_mmWindows=[9,20]
for interval in all_intervals:
	print("interval",interval)
	os.system("rm -rf data/")
	for mmWindow in all_mmWindows:
		print("mmWindow",mmWindow)
		my_history={"BTC":10,"BUSD":1000000}
		mmWindow-=1
		openTrade=0 #0 not trading, 1 selling, 2 buying

		start_date = datetime.strptime('2021 10 23', '%Y %m %d')
		print("start_date",start_date)
		end_date=datetime.strptime('2021 11 06', '%Y %m %d')
		print("end_date",end_date)
		df=pd.DataFrame()
		df=getHistorical(mysymbol,True,"outputs",interval,start_date,end_date)
		log=pd.DataFrame()
		 

		for i in range(mmWindow,(len(df)-mmWindow)):
			
			std_dev=np.std(pd.to_numeric(df.iloc[i-mmWindow:i+1, df.columns.get_loc("close")],downcast="float"))
			average=np.average(pd.to_numeric(df.iloc[i-mmWindow:i+1, df.columns.get_loc("close")],downcast="float"))
			current_price=df.iloc[i, df.columns.get_loc("close")]
			current_date=df.iloc[i, df.columns.get_loc("date")]
			k=2
			upper=average+(std_dev*k)
			lower=average-(std_dev*k)
		
			reach_open=1
			reach_close=0.001
			btc_amount=0.01
			if openTrade == 0:
				#try to open a trade
				if current_price <= reach_open*lower:#TODO
					action="OpenBUY"
					openTrade=2
		#			print("BUY")
		#			sendOrder(spot_client,mysymbol,0.001,"BUY")
					my_history["BTC"]+=btc_amount
					my_history["BUSD"]-=btc_amount*float(current_price)
				elif current_price >= reach_open*upper:#TODO
					action="OopenSELL"
					openTrade=1
		#			print("SELL")
		#			sendOrder(spot_client,mysymbol,0.001,"SELL")
					my_history["BTC"]-=btc_amount
					my_history["BUSD"]+=btc_amount*float(current_price)
				else:
					action="NoTrade"
		#			print(">>>>> NO TRADE <<<<<<")
			else:
				#try to close the open trade
				if average-(average*reach_close) < current_price < average+(average*reach_close):	
					if openTrade == 1:
						my_history["BTC"]+=btc_amount
						my_history["BUSD"]-=btc_amount*float(current_price)
						action="CloseSELL"
					elif openTrade == 2:
						my_history["BTC"]-=btc_amount
						my_history["BUSD"]+=btc_amount*float(current_price)
						action="CloseBUY"
					else:
						action="ERROR"
						print("----------------------------ERROR----------------------------")
								
					openTrade=0
				else:
					action="NoTrade"
		#		print(">>>>> NO TRADE <<<<<<")
			aux={}
			aux[current_date]=[current_price,std_dev,average,upper,lower,my_history["BUSD"],my_history["BTC"],(my_history["BTC"]*current_price)+my_history["BUSD"],action]
			log=pd.concat([log,pd.DataFrame(aux).T])
		log.columns=["current_price","std_dev","average","upper","lower","BUSD","BTC","total_balance","action"]
		log.to_csv("outputs/log-i"+str(interval)+"-w"+str(mmWindow+1)+"-"+(start_date.strftime("%m-%d"))+"to"+(end_date.strftime("%m-%d"))+".csv")
		log.plot()
		#plt.show()
