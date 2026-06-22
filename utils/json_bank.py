import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, 'db', 'bank.json')

def load_bank():
    try:
        with open(FILE, encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}
    
def save_bank(bank):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(
            bank,
            f,
            ensure_ascii= False,
            indent=4
        )