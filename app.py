# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:35:10 2020

@author: sefa
"""

from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import time


def sendSMS():
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC90b1be1f3eff412545349379f0d9b9a3'
    auth_token = 'fa031bed1bf473fd88e38809dc96c9cc'
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
              body=gold_price,
              from_='+12565791581',
              to='+905397722431'
          )
    
    print(message.sid)

while True:
    response = requests.get('http://bigpara.hurriyet.com.tr/altin/')
    soup = BeautifulSoup(response.content, 'html.parser')
    gold_price=soup.find_all('span', class_="value")[1]
    gold_price=str(gold_price)
    gold_price=float(gold_price.split(">")[1].split("<")[0].replace(",", "."))
    if gold_price<450:
        sendSMS()
    
    time.sleep(600)
    print(gold_price)
    

    
