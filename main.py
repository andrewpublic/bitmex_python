from bitmex_websocket import BitMEXWebsocket
from bitmex import bitmex
import logging
from time import sleep
import json
import datetime

def run():
	logger = setup_logger()
	exit = False
	ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD", api_key="APIPUBLIC", api_secret="APIPRIVATE")
  	
	print("\n\n*********************************\nHELLO\n*********************************\n")
	
	while(ws.ws.sock.connected and exit != True):
		'''ws.get_instrument()
		logger.info("Bitcoin: %s\n\n" % ws.get_ticker())'''
		print("Make a selection:\n1. Check price.\n2. Place a limit order.\n3. Place a trailing stop.")
		print("0. Exit.\n")
		result = input("You select: ")
		''' Switch Branching Statement '''
		if result == "0":
			exit = True
		elif result == "1":
			ws.get_instrument()
			logger.info("\n\n\nBitcoin: %s" % ws.get_ticker())
		elif result == "2":
			client = bitmex(test=False, api_key="HrEZHEgnNuYbaNKtYfvA-4AI", api_secret="QTpntb7xCPu0415i7f8iMRUG6t1iEUq0HVKkZiPnVp6x5yer")
			client.Order.Order_new(symbol="XBTUSD", orderQty=int(input()), price=int(input())).result()
		
		print("\n")
		'''sleep(5)'''
		

def setup_logger():
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	ch = logging.StreamHandler()
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	return logger

def myconverter(o):
	if isinstance(o, datetime.datetime):
		return o.__str__()

if __name__ == "__main__":
	run()
