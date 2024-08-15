import os
from dotenv import load_dotenv

def get_params():
    chat_params = {
        'api_key': os.getenv('OPENAI_KEY'),
        'model': os.getenv('OPENAI_MODEL'),
        'max_tokens': os.getenv('MAX_TOKENS'),
        'temperature': os.getenv('MODEL_TEMP'),
        'n': os.getenv('NO_OF_COMPLETIONS'),
        'top_p': os.getenv('TOP_P'),
        'freq_pen': os.getenv('FREQ_PENALTY'),
        'pres_pen': os.getenv('PRES_PENALTY')
    }

    return chat_params
    
