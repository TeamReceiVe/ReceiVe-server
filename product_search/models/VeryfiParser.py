from veryfi import Client
from abc import ABC
import json
import os

class VeryfiParser():
    def __init__(self,filename: str) -> None:

        #for authentication
        self.client_id = 'vrfZHS0FN8frHYeHt3ozsUk7uhJZZ54L3Y4rtnL'
        self.client_secret = 'u6WD5AuzmfgsW5ORPRGOs9vP2vK7VGeH022KhZ2iVVaHkrpHFzYyJeddo0w9WLVejOvaBRw3Epm4kltKV64kui84ROwV7vT8t4Uyy7TaHYJnDCC8ErUOALmge0InsCeC'
        self.username = 'ar2237'
        self.api_key = '23470b1b176963fb59717d032d5f8c92'

        #to be sent to the veryfiAPI
        self.categories = ['Grocery', 'Utilities', 'Travel']
        self.file_path = filename


        self.items = None
        self.response = None

    def get_response(self) -> None:
        if os.path.isfile("response.json"):
            response = json.loads("response.json")
        else:
            veryfi_client = Client(self.client_id, 
                                    self.client_secret, 
                                    self.username, 
                                    self.api_key)
            
            response = veryfi_client.process_document(self.file_path, 
                                                        categories=self.categories)
            self.response = response
            json.dumps(self.response)

    def get_date(self) -> str:
        if self.items == None:
            self.get_response()
        
        return self.response["created_date"]
        
    def get_line_items(self):
            if self.items == None:
                self.get_response()

            self.items = list()
            for item in self.response["line_items"]:
                self.items.append(tuple([item['description'], item['total']]))

            return self.items
