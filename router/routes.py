from flask import jsonify, render_template, request, redirect, url_for
from app import app
import sys
import os

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from src import extract_text
from src import gen_response

@app.route('/chat')
def chat():
    return render_template('chat.html')
    

@app.route('/get-content', methods=['POST'])
def get_content():
    data = request.get_json()
    filepath = data.get('filepath')
    
    if filepath and os.path.isfile(filepath):
        fileContent = extract_text(filepath)
        print(fileContent)
        return jsonify({"content": fileContent})

@app.route('/gen-sum', methods=['POST'])
def gen_sum():
    data = request.get_json()
    try:
        result = gen_response.gen_response(data)

        response = {
            'user_prompt': result['user_prompt'],
            'prompt_response': result['prompt_response'],
            'runtime': result['runtime'],
            'input_tokens': result['input_tokens'],
            'output_tokens': result['output_tokens']
        }

        return jsonify(response), 200
    
    except Exception as e:
        error_res = {
            'error': str(e)
        }

        return jsonify(error_res), 500



