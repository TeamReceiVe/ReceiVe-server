import requests

# Define the URL to which you want to send the POST request
url = 'http://127.0.0.1:5000/upload'


# Path to the image file you want to upload
image_path = './test.png'

# Open the image file in binary mode
with open(image_path, 'rb') as file:
    # Prepare the data to be sent in the POST request
    files = {'image': file}
    
    # Send the POST request with the image attached
    response = requests.post(url, files=files)

# Send the POST request
#response = requests.post(url, data=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("POST request was successful!")
    print("Response:", response.text)
else:
    print("POST request failed with status code:", response.status_code)

