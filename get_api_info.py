import requests

url = "https://api.topmediai.com/v1/get_api_key_info"
headers = {
    "accept": "application/json",
    "x-api-key": "1b547580cfd44b27b1647aec0fafcddc"
}

response = requests.get(url, headers=headers)

# The response body is a JSON string, so we parse it into a Python dictionary
data = response.json()

# Now, data is a Python dictionary that contains the response body
print(data)
