# Python handler for the Demio API
# 
# Author: Sebastian Latorre
# 
# Created: 2020-12-16
# Last Update: 2020-12-16

import requests
from urllib.request import urlopen
from django.conf import settings

class DemioAPI():
    api_key = ""
    api_secret = ""
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def ping(self):
        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret
        }
        response = requests.get('https://my.demio.com/api/v1/ping', headers=headers) 
        
        return True if response.json()['pong'] else False
    
    @property
    def events(self):
        if not self.ping:
            return False
        
        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret
        }
        response = requests.get('https://my.demio.com/api/v1/events', headers=headers) 
        
        return response.json()
    
    @property
    def upcoming_events(self):
        if not self.ping:
            return False

        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret,
        }
        response = requests.get('https://my.demio.com/api/v1/events?type=upcoming', headers=headers) 
        
        return response.json()

    
    def event(self, id, active=False):
        if not self.ping:
            return False

        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret,
        }
        response = requests.get('https://my.demio.com/api/v1/event/'+str(id)+'?active='+str(active).lower(), headers=headers) 
        
        return response.json()
    
    
    def event_date(self, event_id, date_id):
        if not self.ping:
            return False

        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret,
        }
        response = requests.get('https://my.demio.com/api/v1/event/'+str(event_id)+'/date/'+str(date_id), headers=headers) 
        
        return response.json()
    
    # STATUS can be:
    #   attended
    #   did-not-attend
    #   completed
    #   left-early
    #   banned
    def event_date_participants(self, date_id, status):
        if not self.ping:
            return False

        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret,
        }
        response = requests.get('https://my.demio.com/api/v1/report/'+str(date_id)+'/participants?status='+status, headers=headers) 
        
        return response.json()


    def register(self, event_id, first_name, last_name, email):
        if not self.ping:
            return False

        headers = {
            'Api-Key': self.api_key,
            'Api-Secret': self.api_secret,
        }
        data={
            'id': event_id,
            'name': first_name,
            'last_name': last_name,
            'email': email,
        }
        response = requests.put('https://my.demio.com/api/v1/event/register', json=data, headers=headers ) 
        
        return response.json()