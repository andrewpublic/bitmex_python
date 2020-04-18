#What are we trying to do?

from bitmex_websocket import BitMEXWebsocket
from bitmex import bitmex
import logging
from time import sleep
import json
import datetime
from tkinter import *

ws : BitMEXWebsocket

def exit():
	return

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
        
def connect():
    global ws
    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD", api_key="D_SHkcuhB2jeYRokZKcqL8RI", api_secret="K8kVlJ9T-3ELJukEdiXsLTpbQH8O8IioCnAqw2naf--Uy0ZL")
    print("\n\n*********************************\nHELLO\n*********************************\n")
    c.pack()
    d.pack()
    
def end():
    quit()
    
def checkprice():
    global ws
    ws.get_instrument()
    logger.info("\n\n\nBitcoin: %s" % ws.get_ticker())

#GUI:

root = Tk()
root.geometry('300x300')

l = Label(root, text="Hello World!")
l.pack()

b = Button(root, text="Connect", command=connect)	
b.pack()

c = Button(root, text="Check price", command=checkprice)

d = Button(root, text="Exit", command=end)

logger = setup_logger()

root.mainloop()