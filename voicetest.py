import requests
import json

def text_to_speech():
    url = "https://api.topmediai.com/v1/text2speech"
    headers = {
        "accept": "application/json",
        "x-api-key": "1b547580cfd44b27b1647aec0fafcddc",
        "Content-Type": "application/json"
    }

    # Get user input
    text = input("Enter the text you want to convert to speech: ")

    data = {
      "text": text,
      "speaker": "00151554-3826-11ee-a861-00163e2ac61b",
      "emotion": "Neutral"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # The response body is a JSON string, so we parse it into a Python dictionary
    data = response.json()

    # Print the oss_url to the screen
    print(data['data']['oss_url'])

    # Return the oss_url
    return data['data']['oss_url']

# Call the function

print(text_to_speech())