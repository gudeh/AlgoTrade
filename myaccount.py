import logging
import time
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError
from Utils import mytest, readOnly
import pprint
import requests
import pandas as pd
pp = pprint.PrettyPrinter(width=10,indent=5,depth=3)

# config_logging(logging, logging.DEBUG)

# key = mytest.API_KEY
# secret = mytest.API_SECRET
# client = Client(key, secret, base_url="https://testnet.binance.vision")

key = readOnly.API_KEY
secret = readOnly.API_SECRET
client = Client(key, secret)

spot_dict={}
save_dict={}
total_usdt=0.0

r = requests.get("https://api.binance.com/api/v3/ticker/price")

#search for all pairs with BTC, USDT, BUSD or BRL
all_list= set()
acc=client.account()
balance=acc['balances']
for b in balance:
	if float(b['free'])>0: 
			#REMOVED FOR PRIVACY
		if aux[:2] == 'LD':
			aux=aux[2:]
		if aux in spot_dict:
			#REMOVED FOR PRIVACY
		else:
			#REMOVED FOR PRIVACY
		all_list.add(aux)
print("spot_dict")
print(len(spot_dict))
pp.pprint(spot_dict)
print('all_list',sorted(all_list))


#TODO trocar esse laco em uma lista de dicts por um unico dict com acesso direto
price_json = r.json()
prices_dict = {}
all_prices={}
for d in price_json:
	all_prices[d['symbol']]=d['price']
print("all_prices")
pp.pprint(all_prices)
for known_name in all_list:
	for item in price_json:
		#REMOVED FOR PRIVACY
		if name.find(#REMOVED FOR PRIVACY)
			#REMOVED FOR PRIVACY	



#TODO somar spot com earn
all_paid = pd.DataFrame()#(dtype=np.int8)
all_trades=[]
trade_volume={}
avrg_price={}
realized_profit={}
potential_profit={}
current_avrg_price={}
for single_name in spot_dict:
	trade_volume[single_name]=0.0
	avrg_price[single_name]=0.0
	current_avrg_price[single_name]=0.0
#	realized_profit[single_name]=0.0
#	potential_profit[single_name]=0.0
my_list=["BRL","USDT","BUSD"]#,"BTC"]
#for terrible in my_list:
for single_name in spot_dict:
	pair_name=""
	# print("\n\n\n\n\nDOING ",terrible)
#	for single_name in spot_dict:
	for terrible in my_list:
		quote_sum=0.0
		quant_sum=0.0
		average_price=0.0
		total_volume=0.0
		print(single_name,"+",terrible)
		if prices_dict.get(terrible+single_name)!=None:
			#REMOVED FOR PRIVACY
		elif prices_dict.get(single_name+terrible)!=None:
			#REMOVED FOR PRIVACY
		else:
			resp=''
			pair_name=''
		print(pair_name)
		pp.pprint(resp)
		for trade in resp:
			# pp.pprint(trade)
			if trade['isBuyer']==True:
				#REMOVED FOR PRIVACY
			else:
				place="SELL"
				#REMOVED FOR PRIVACY
			print(pair_name,quote_sum,quant_sum)
			all_trades.append([pair_name,place,float(trade['price']),float(trade['qty']),float(trade['quoteQty']),float(trade['commission']),trade['commissionAsset']])
		if(quant_sum!=0):
			current_price=float(all_prices[pair_name])
			if terrible=="BRL":
				#REMOVED FOR PRIVACY
			average_price=abs(quote_sum/quant_sum)
			diff=current_price-average_price
			print("single_name,spot_dict[single_name]",single_name,spot_dict[single_name])
			volume=quant_sum
			trade_volume[single_name]=trade_volume[single_name]+volume
			if avrg_price[single_name]>0:
				#REMOVED FOR PRIVACY
			else:
				#REMOVED FOR PRIVACY
			if current_avrg_price[single_name]>0:
				#REMOVED FOR PRIVACY
			else:
				current_avrg_price[single_name]=current_price
				
			all_paid[pair_name]=[average_price,current_price,diff,volume,abs(volume)*diff]
			print(pair_name,average_price,current_price,diff,volume,abs(volume)*diff)

print(pd.DataFrame(all_trades,columns=["pair","place","price","quantity","total_paid","fee_amount","fee_type"]).to_csv("all_trades.csv"))
all_paid=all_paid.T
all_paid.columns=["average price","current price","diff","volume","volume*diff"]
pp.pprint(all_paid)
print("trade_volume")	
pp.pprint(trade_volume)
print("avrg_price")	
pp.pprint(avrg_price)
for single_name in spot_dict:
	if trade_volume[single_name]<=0:
		realized_profit[single_name]=(abs(trade_volume[single_name]))*(avrg_price[single_name])
	else:
		potential_profit[single_name]=(trade_volume[single_name])*(current_avrg_price[single_name]-avrg_price[single_name])
print("realized_profit")	
pp.pprint(realized_profit)
print("potential_profit")	
pp.pprint(potential_profit)
# all_paid = all_paid.sort_index()
all_paid = all_paid.sort_values(by=all_paid.columns[2])
all_paid=all_paid.sort_index()
pp.pprint(all_paid)
# print(type(all_paid))
all_paid.to_csv('out.csv')
