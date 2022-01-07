from datetime import *
import pandas as pd
import os
from zipfile import ZipFile
import glob
from pathlib import Path
import requests
import pprint
pp = pprint.PrettyPrinter(width=10,indent=5,depth=3)
import logging
from binance.lib.utils import config_logging
from binance.error import ClientError
from binance.spot import Spot as Client #REST option

def getHistorical(pair_name,do_download,out_path,interval_size,start_date,end_date):
	source = os.getcwd()
#	mypath= source#+"\\temp"
	mypath=Path(source)
	now_date = datetime.now()
	if not end_date:
		command="python3 download-kline.py -s "+pair_name+" -i "+interval_size+" -endDate "+now_date.strftime("%Y-%m-%d")
	else:
		command="python3 download-kline.py -s "+pair_name+" -i "+interval_size+" -endDate "+end_date.strftime("%Y-%m-%d")
#	command="python3 download-kline.py -s "+pair_name+" -endDate "+now_date.strftime("%Y-%m-%d")
	if start_date!="":		
		command=command+" -startDate "+start_date.strftime("%Y-%m-%d")
	print(command)
	if(do_download):
		os.system(command)
	print("Finished download!")
	li=[]
	
	#set daily
	if interval_size!="1m" and interval_size!="5m" and interval_size!="1h" and interval_size!="2h":
		daily_path=mypath / "data/spot/daily/klines"/pair_name/interval_size#"1d/"
	else:
		my_str=str(start_date.strftime("%Y-%m-%d"))+"_"+str(end_date.strftime("%Y-%m-%d"))
		daily_path=mypath / "data/spot/daily/klines"/pair_name/interval_size/my_str
	print("daily_path",daily_path)
	
	#extract from monthly to daily
	if interval_size!="1m" and interval_size!="5m" and interval_size!="1h" and interval_size!="2h":
		monthly_path=mypath / "data/spot/monthly/klines"/pair_name/interval_size#"1d/"
		files = [f for f in os.listdir(monthly_path) if f.endswith(".zip")]
		for f in files:
	#		with ZipFile(monthly_path+f, 'r') as zipObj:
			with ZipFile(monthly_path/Path(f), 'r') as zipObj:
				zipObj.extractall(daily_path)
	#extract from daily to daily
	if os.path.exists(daily_path):
		files = [f for f in os.listdir(daily_path) if f.endswith(".zip")]
		for f in files:
			with ZipFile(daily_path/Path(f), 'r') as zipObj:
				zipObj.extractall(daily_path) #extracting everything to monthly_path
	  
	my_header=["date","open","high","low","close","volume","close_time","Quote_asset_volume","Number_of_trades","Taker_buy_base_asset_volume","Taker_buy_quote_asset_volume","Ignore"]

	all_files = glob.glob(str(daily_path) + "/*.csv")
	print("all_files",all_files)
#	all_files = glob.glob(monthly_path / "*.csv")
	for filename in all_files:
		df = pd.read_csv(filename,names=my_header)#, index_col=None, header=0)
		# print(df.head)
		li.append(df)


	print(df.shape)
	print(len(li))

	frame = pd.concat(li,names=my_header, axis=0,ignore_index=True)
	frame['date']=pd.to_datetime(frame['date'],unit='ms')
	frame['close_time']=pd.to_datetime(frame['close_time'],unit='ms')
	frame=frame.sort_values(by=['date'])
	print(frame.shape)
	print(frame.head)
	frame.to_csv(out_path+"/"+pair_name+".csv")#(source+pair_name+".csv")
	return frame
	
def printInfos():
#	info = requests.get("https://testnet.binancefuture.com")
	info = requests.get("https://testnet.binance.vision/api/v3/exchangeInfo")
	info_json= info.json()
	pp = pprint.PrettyPrinter(indent=0)
	#pp.pprint(info_json)
	infos_dict = {}
	for item in info_json['symbols']: #list of dicts
		name=item['symbol']
		status=item['status']
		permission=item['isSpotTradingAllowed']
		infos_dict[name]=[status,permission]
	#pprint(infos_dict)
	print(type(infos_dict))
	print(infos_dict)


def getAccInfo(spot_client):
	acc=spot_client.account()
	balance=acc['balances']
	spot_dict={}
	all_list= set()
	for b in balance:
		if float(b['free'])>0: 
#			print (type(b),b)
			aux=b['asset']
			if aux[:2] == 'LD':
				aux=aux[2:]
			if aux in spot_dict:
				spot_dict[aux]=float(spot_dict[aux])+float(b['free'])
			else:
				spot_dict[aux]=float(b['free'])
			all_list.add(aux)
	print("spot_dict")
	print(len(spot_dict))
	pp.pprint(spot_dict)
	print('all tokens in spot',sorted(all_list))
	return spot_dict
	
def sendOrder(spot_client,mysymbol,amount,side):
	print("Send order",mysymbol,side,amount)
	params = {
		"symbol": mysymbol,#"BTCUSDT",
		"side": side,#"BUY",
		"type": "MARKET",#"LIMIT",
#		"timeInForce": "GTC",
		"quantity": amount,
#		"price": 9500,
	}
	try:
	    response = spot_client.new_order(**params)
	    logging.info(response)
	except ClientError as error:
	    logging.error(
		"Found error. status: {}, error code: {}, error message: {}".format(
		    error.status_code, error.error_code, error.error_message))	
		    
#def fakeSend(mysymbol,amount,side,history):
	
