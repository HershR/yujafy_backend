from flask import Blueprint, request, jsonify, current_app
from flask_cors import CORS, cross_origin
from .request_utils import ID, SENTENCES, VOICE, check_json_post_args, check_get_args
import requests
import json

bp = Blueprint('api', __name__)

API_KEY = "06085097256849a3a7b5f837c4583363"

FILE_PATH = "./audiofiles"

DEFAULT_VOICE = "0015548d-3826-11ee-a861-00163e2ac61b"

@bp.route('/api/process', methods=['POST'])
@cross_origin()
def process_text():
    # write up def
    """
    :param: sentences: List , voice: AI voice
    :return:
    """
    _, error = check_json_post_args([SENTENCES, VOICE])
    if error:
        return jsonify(error), 400
    url = "https://api.topmediai.com/v1/text2speech"
    v_id = request.json.get(ID)
    sentences = request.json.get(SENTENCES)
    voice_id = DEFAULT_VOICE if request.json.get(VOICE) == 'default' else request.json.get(VOICE)
    print(sentences, voice_id)
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    audio_links = []
    for sentence in sentences:
        chunks = split_string(sentence, 200)

        # links = []

        for chunk in chunks:
            param = {
                "text": chunk.replace('\ufeff', ''),
                "speaker": voice_id,
                "emotion": "Neutral"
            }

            r = requests.post(url, headers=headers, data=json.dumps(param))

            # The response body is a JSON string, so we parse it into a Python dictionary
            if r.status_code == 200:
                data = r.json()
                try:
                    print(chunk, data['data']['oss_url'])
                    audio_links.append(data['data']['oss_url'])
                except BaseException as e:
                    print(e)
                    print(chunk)
                    print('data', data)
            else:
                print(r)
                # links.append(None)
        # audio_links[len(audio_links)] = links
    file_name = f'{FILE_PATH}\{v_id}.json'

    # import os
    # current_directory = os.getcwd()
    # print(f"The current working directory is: {current_directory}")

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

def split_string(input_string, max_length):
    result = []

    for i in range(0, len(input_string), max_length):
        result.append(input_string[i:i + max_length])

    return result
