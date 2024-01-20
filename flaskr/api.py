from flask import Blueprint, request, jsonify
from request_utils import SENTENCES, VOICE, check_json_post_args, check_get_args

bp = Blueprint('api', __name__)


@bp.route('/api/process', method=['POST'])
def process_text():
    # write up def
    """
    :param: sentences: List , voice: AI voice
    :return:
    """
    data, error = check_json_post_args([SENTENCES, VOICE])
    if error:
        return jsonify(error), 400
    # else work with data


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
