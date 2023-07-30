from datetime import datetime
from utils import format_date, mask_card_number, mask_account_number, read_operations_from_file

operations = read_operations_from_file()

sorted_operations = sorted(
    [op for op in operations if op.get('state') == 'EXECUTED'],
    key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
    reverse=True
)

for operation in sorted_operations[:5]:
    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation['description'] if 'description' in operation else 'Н/Д'
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    from_account = operation['from'] if 'from' in operation else 'Н/Д'
    to_account = operation['to'] if 'to' in operation else 'Н/Д'

    card_number = from_account.split()[-1] if 'from' in operation else ''
    account_number = to_account.split()[-1] if 'to' in operation else 'Н/Д'

    card_masked = mask_card_number(card_number) if card_number != '' else ''
    account_masked = mask_account_number(account_number) if account_number != 'N/A' else 'Н/Д'

    card_name = from_account.split()[0] if 'from' in operation else 'Счет'

    print(f"{date}  {description}")
    print(f"{card_name} {card_masked} -> {account_masked}")
    print(f"{amount} {currency}")
    print()