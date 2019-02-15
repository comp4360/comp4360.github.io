#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Şükrü Ozan, Ph.D. 24.10.2018

import json 
import requests
import time
import python_forex_quotes

TOKEN = "653296112:AAG5oWLVI0QCtj2HtQy5KyN5Mx9d4rh4DuM"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
client = python_forex_quotes.ForexDataClient('zpTm0lyoGtmDgWKB51wKMhpinDeLoCPN')

symbols = client.getSymbols()

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates?limit={}&offset={}".format("10", "-1") 
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    message_id = updates["result"][last_update]["message"]["message_id"]
    from_username =  updates["result"]
    return (text, chat_id, message_id,from_username)

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)    

def send_message(text, chat_id, parse='HTML'):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, chat_id,parse)
    get_url(url)

def reply_message(text, chat_id, message_id):
    url = URL + "sendMessage?text={}&reply_to_message_id={}&chat_id={}".format(text,message_id,chat_id)
    get_url(url)

def main():
	updates = get_updates()
	last_update_id = get_last_update_id(updates)
	text, chat_id, message_id,from_username = get_last_chat_id_and_text(updates)			
	wordlist = text.split()
	send_message("<b> BOT STARTED </b>",'52876446', 'HTML')
	try:		
		quote_list = []
		for word in wordlist:
			if  word.upper() in symbols:
				quote_list.append(word.upper())
		
		if len(quote_list)>0:
			response = client.getQuotes(quote_list)
			message = "<b>"
			for result in response:
				message +=  str(result['symbol'])+":"+str(result['price'])+"\n"
			message += "</b>"
			send_message(message, chat_id,'HTML')	
			send_message("<b> A REQUEST HAS BEEN MADE! by " + str(from_username) + "</b>",'52876446', 'HTML')
			exit
	except:
		send_message("<b> BOT F*CKED UP! </b>",'52876446', 'HTML')
	send_message("<b> BOT ENDED </b>"+str(last_update_id),'52876446', 'HTML')

if __name__ == '__main__':
    main()
    
    
#print client.quota()
#for symbol in symbols:
#	print(symbol)
#curr_list = ['USD','TRY','EUR','GBP','CAD','JPY','BTC']
#lang_list = ['tr','en','fr','de']
#dict_replace = { 'ı':'i','İ':'I','ö':'o','Ö':'O','ü':'u','Ü':'U','ç':'c','Ç':'C','ş':'s','Ş':'S','ğ':'g','Ğ':'G'}
#special_list = ['sik','amk','amina','aq','yarak','yarrak','amcik','sikik','ibne','ibnelik','a.q.','am','got','siker','sikerler','yavsak']
#https://api.telegram.org/bot653296112:AAG5oWLVI0QCtj2HtQy5KyN5Mx9d4rh4DuM/getUpdates?limit=10&offset=-1
#text, chat = get_last_chat_id_and_text(get_updates())
#send_message(text, chat)
'''
if wordlist[0] in lang_list:
keyword = ' '.join(wordlist[2:])
#print(keyword)
translation = translate(wordlist[0],wordlist[1],keyword)
text = translation.origin+' -> '+translation.text.encode('utf-8')
#print(text)

if word in special_list:
reply_message("Ooops you did it again!" , chat_id,message_id) 
"""             
elif text == "Sinan":
text = "Sinan'in amk"
print(text,chat,last_update_id)
send_message(text, chat)
"""
						
				#text = text.encode('utf-8')
				#tmp = unturkify(text)
				
def translate(src,dest,keyword):
    translator = Translator()
    result = translator.translate(keyword,src=src,dest=dest,)
    return result

def unturkify(input):
    for i,j in dict_replace.iteritems():
        input = input.replace(str(i),str(j))
    return input
#from googletrans import Translator			
'''