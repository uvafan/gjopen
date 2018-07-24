import requests
import json

def getStockData(symbol,key,full):
	request_txt = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sym}&apikey={k}'.format(sym=symbol,k=key)
	if full:
		request_txt += '&outputsize=full'
	info = requests.get(request_txt)
	return info.text

def main():
	f = open('alpha_vantage_api_key.txt', 'r')
	alpha_vantage_key = f.read().strip()
	spy_data = getStockData('SPY',alpha_vantage_key,True)
	print(json.loads(spy_data))

main()