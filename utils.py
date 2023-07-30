import json
from datetime import datetime

def read_operations_from_file():
    with open('operations.json', 'r', encoding='utf-8') as f:
        operations = json.load(f)
    return operations

def format_date(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

def mask_card_number(card_number):
     formatted_mask_number= card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
     return formatted_mask_number

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"