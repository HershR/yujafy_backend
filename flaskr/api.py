import flask
from flask import Blueprint, request, jsonify, current_app
from flask_cors import CORS, cross_origin
from .request_utils import ID, SENTENCES, VOICE, check_json_post_args, check_get_args
import textwrap
import requests
import json

bp = Blueprint('api', __name__)

API_KEY = "1b547580cfd44b27b1647aec0fafcddc"

FILE_PATH = './audiofiles'


@bp.route('/api/process', methods=['POST'])
@cross_origin()
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
    v_id = request.json.get(ID)
    sentences = request.json.get(SENTENCES)
    print(sentences)
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    audio_links = {}
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
                print(chunk, data['data']['oss_url'])
                links.append(data['data']['oss_url'])
            else:
                print(r)
                links.append(None)
        audio_links[len(audio_links)] = links
    file_name = f'{FILE_PATH}\{v_id}.json'

    #import os
    #current_directory = os.getcwd()
    #print(f"The current working directory is: {current_directory}")

    with open(file_name, 'w') as json_file:
        json.dump(audio_links, json_file, indent=4)
    return jsonify({'data': audio_links}), 200


@bp.route('/api/retrieve', methods=['GET'])
@cross_origin()
def retrieve_audio():
    # write up def
    """
    :param: v_id: video id
    :return:
    """
    v_id = request.args.get('v_id', default='none', type=str)
    print(v_id)
    # else work with data
    file_path = f"{FILE_PATH}/{v_id}.json"
    try:
        with open(file_path, 'r') as json_file:
            audio_links = json.load(json_file)
    except BaseException as e:
        print('error', e)
        return jsonify("error: Unable to find file audio files corresponding to ID"), 404
    return jsonify({'data': audio_links}), 200

# /v1/voices_list
