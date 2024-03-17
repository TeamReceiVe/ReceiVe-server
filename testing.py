import requests

def get_user_agent():
    try:
        # Send a GET request to a dummy URL
        response = requests.get('https://www.sainsburys.co.uk/gol-ui/product/sainsburys-cheese---onion-pizza')
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Print the user-agent header from the response
        print("User-Agent:", response.request.headers['User-Agent'])

    except requests.RequestException as e:
        print("Error fetching user-agent:", e)

# Call the function to get the user-agent
get_user_agent()