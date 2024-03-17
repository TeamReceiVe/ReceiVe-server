from flask import Flask, request, jsonify
#from flask_cors import CORS

import json
from product_search.models.Product import Product
from serpapi import GoogleSearch

import requests
from bs4 import BeautifulSoup

#find receipts
from veryfi import Client
from abc import ABC
import json
import os

from product_classification.working import receipt_score



app = Flask(__name__)
#CORS(app)



def search_product(input_product : Product):
    link,imlink = get_product_link(input_product)

    #print('here')
    #print(link)
    #print(imlink)
    input_product.populate_product_using_link(link)
    return input_product

def get_product_link(array):
    name_on_receipt = array[0]

    price_in_pounds = array[1]
    # returns [pounds, pence] in int

    search_query : str = f"{name_on_receipt} £{price_in_pounds} Sainsbury's"
    # e.g. "cocoa powder £3.15 site:https://www.sainsburys.co.uk/"

    private_api_key = "49e5a4ce4fe4d94be42dbd3ed06605cc55e20c85002bcadebe422993536c8fd9"



    params = {
    "q": search_query,
    "hl": "en",
    "gl": "uk",
    "google_domain": "google.com",
    "api_key": private_api_key
    }

    search = GoogleSearch(params)

    results = search.get_dict()
    link = __get_link_from_results(results)
    try:
        image_link = results["inline_images"][0]["original"]
    except:
        image_link = ""
    #print(link,image_link)
    return link, image_link

def __get_link_from_results(results):
    return results["organic_results"][0]["link"]

class VerifyParser():
    def __init__(self, filename: str) -> None:
        self.client_id = 'vrfZHS0FN8frHYeHt3ozsUk7uhJZZ54L3Y4rtnL'
        self.client_secret = 'u6WD5AuzmfgsW5ORPRGOs9vP2vK7VGeH022KhZ2iVVaHkrpHFzYyJeddo0w9WLVejOvaBRw3Epm4kltKV64kui84ROwV7vT8t4Uyy7TaHYJnDCC8ErUOALmge0InsCeC'
        self.username = 'ar2237'
        self.api_key = '23470b1b176963fb59717d032d5f8c92'
        self.categories = ['Grocery', 'Utilities', 'Travel']
        self.file_path = filename
        self.items = None
        self.response = None

    def get_response(self) -> None:
        #if os.path.isfile("response.json"):
         #   response = json.loads("response.json")
        #else:
        veryfi_client = Client(self.client_id,
                                self.client_secret,
                                self.username,
                                self.api_key)

        response = veryfi_client.process_document(self.file_path,
                                                      categories=self.categories)
        self.response = response
        with open("response.json", "w") as f:
            json.dump(self.response, f)

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

def is_vegan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the section containing product information
            product_info = soup.find('div', class_='productSummary')
            
            # Find the section containing dietary information
            dietary_info = product_info.find('div', class_='tableWrapper')
            
            # Find all the rows in the dietary information section
            rows = dietary_info.find_all('tr')
            
            # Loop through each row and check if it contains 'Suitable for vegans' label
            for row in rows:
                if 'Suitable for vegans' in row.text:
                    return True
            return False
        else:
            #print("Failed to fetch URL:", url)
            return None
    except Exception as e:
        #print("An error occurred:", e)
        return None

@app.route('/upload', methods=['POST'])

def upload_image():
    if 'image' in request.files:
        image_file = request.files['image']
        image_file.save('uploaded_image.jpeg')
        filename = 'uploaded_image.jpeg'
        parser = VerifyParser(filename)
        items = parser.get_line_items()
        for i in items:
            if i[1] <= 0:
                items.pop[i]
        #items = [('MONSTER PIPELINE', 1.85), ('BRIE, BACON & CHILLI', 3.0), ('PIZZA SWIRL', 1.1)]
        #print (items)

        
        score = receipt_score(items)
        

        for i in items:
            if i[1] <= 0:
                break
            #else:
                #pass
            get_product_link(i)
        response_data = {'status': 'success', 'message': 'Image uploaded successfully!'}
    else:
        response_data = {'status': 'error', 'message': 'No image found in the request.'}

    return jsonify(response_data)

if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)


