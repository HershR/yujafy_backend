# yujafiy_backend
Backend of for tts Yuja videos
Currently made to be run locally

# Set Up
1. install packages in requirments.txt with "pip install -r requirements.txt"
2. get API key from [topmediai.com](https://www.topmediai.com/api/text-to-speech-api/)
3. in ./flaskr/api.py replace API key var
4. run server with 
```
$ python run.py
```
5. Server should start, if you have issue with using port 5000, edit the port in run.py and all api calls in the frontend extension

# Cache
All processed videos are saved and can be retrieved
Audio file url are stored in ./audiofiles. Each file uses the following naming convention "videoPid_voiceId.json"
Each file stores a list of urls. 

