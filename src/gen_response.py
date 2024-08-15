from flask import json
import openai
import time
from src import gen_sys_prompt
from src import gen_user_prompt
from src import get_params

def gen_response(data):

    try:
        ## creating openAI message
        sys_prompt = gen_sys_prompt.gen_sys_prompt(data['sys_prompt'])
        user_prompt = gen_user_prompt.gen_user_prompt(data['document'], data['intent'], data['tone'], data['length'], data['focus'], data['target_audience'], data['emphasis'], data['customization'])
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]

        chat_params = get_params.get_params()

        ## starting time and generating response
        openai.api_key = chat_params['api_key']
        start_time = time.time()

        response = openai.chat.completions.create(
            model=chat_params['model'],
            messages=messages,
            max_tokens=int(chat_params['max_tokens']),
            temperature=float(chat_params['temperature']),
            n=int(chat_params['n']),
            top_p=float(chat_params['top_p']),
            frequency_penalty=float(chat_params['freq_pen']),
            presence_penalty=float(chat_params['pres_pen'])
        )

        end_time = time.time()

        ### creating the total response data
        responseData = {
            "prompt_response": response.choices[0].message.content,
            "user_prompt": user_prompt,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "runtime": end_time - start_time
        }
        return responseData
    except Exception as e:
        print("Error here.....")
        print(e)
        return str(e)
