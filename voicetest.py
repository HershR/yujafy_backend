import requests
import json
import textwrap

def text_to_speech():
    url = "https://api.topmediai.com/v1/text2speech"
    headers = {
        "accept": "application/json",
        "x-api-key": "1b547580cfd44b27b1647aec0fafcddc",
        "Content-Type": "application/json"
    }

    # Get user input
    text = input("Enter the text you want to convert to speech: ")

    # Split the text into chunks of up to 250 characters without splitting words
    chunks = textwrap.wrap(text, width=250)

    urls = []

    for chunk in chunks:
        data = {
          "text": chunk,
          "speaker": "00151554-3826-11ee-a861-00163e2ac61b",
          "emotion": "Neutral"
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        # The response body is a JSON string, so we parse it into a Python dictionary
        data = response.json()

        # Check if 'data' is in the response
        if 'data' in data:
            # Print the oss_url to the screen
            print(data['data']['oss_url'])

            # Add the oss_url to the list
            urls.append(data['data']['oss_url'])
        else:
            print("Error: 'data' not in response")

    # Return the list of oss_urls
    return urls

# Call the function
print(text_to_speech())
