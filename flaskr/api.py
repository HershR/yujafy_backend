import flask
from flask import Blueprint, request, jsonify
from .request_utils import SENTENCES, VOICE, check_json_post_args, check_get_args
import textwrap
import requests
import json

bp = Blueprint('api', __name__)

API_KEY = "1b547580cfd44b27b1647aec0fafcddc"


# FILE_PATH = flask.Config['FILE_PATH']


@bp.route('/api/process', methods=['POST'])
def process_text():
    # write up def
    """
    :param: sentences: List , voice: AI voice
    :return:
    """
    data, error = check_json_post_args([SENTENCES, VOICE])
    if error:
        return jsonify(error), 400
    url = "https://api.topmediai.com/v1/text2speech"
    sentences = request.json.get(SENTENCES)
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    audio_links = []
    for sentence in sentences:
        chunks = textwrap.wrap(sentence, width=250)

        links = []

        for chunk in chunks:
            data = {
                "text": chunk,
                "speaker": "0015548d-3826-11ee-a861-00163e2ac61b",
                "emotion": "Neutral"
            }

            r = requests.post(url, headers=headers, data=json.dumps(data))

            # The response body is a JSON string, so we parse it into a Python dictionary
            if r.status_code == 200:

                data = r.json()
                print(data['data']['oss_url'])
                links.append(data['data']['oss_url'])
            else:
                print(r)
                links.append(None)
        audio_links.append(links)
    return jsonify({'data': audio_links}), 200


'''
@bp.route('/api/retrieve', method=['GET'])
def retrieve_audio():
    # write up def
    """
    :param: video_name: String , index: int, video marker
    :return:
    """
    data, error = check_json_post_args([SENTENCES, VOICE])
    if error:
        return jsonify(error), 400
    # else work with data
    file_name = data['video_name']
    sound_index = data['index']
    file_path = f"{FILE_PATH}/{file_name}.txt"
    sound_url = None
    error = "sound file does not exist"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if 0 <= sound_index < len(lines):
            desired_line = lines[sound_index]
            sound_url = desired_line
        else:
            print(f"Line {sound_index} is out of range for the file.")
            error = "index out of bounds"
    if not sound_url:
        return jsonify(error), 400
    return jsonify({'url': sound_url}, 200)
'''
# /v1/voices_list
