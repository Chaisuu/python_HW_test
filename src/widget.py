def get_mask_card_number(card_number: str) -> str:
    """Функция которая возвращает маску карты"""
    return card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]


def get_mask_account(card_number: str) -> str:
    """Функция которая маскирует номер счета"""
    return "**" + card_number[-4:]

def mask_account_card(numbers: str) -> str:
    if len(numbers.split()[1]) == 16:
        new_card_mask = get_mask_card_number(numbers.split()[1])
        result = f'{numbers[:-16]}{new_card_mask}'


    elif len(numbers.split()[1]) == 20:
        new_card_chet = get_mask_account(numbers.split()[1])
        result = f'{numbers[:-20]}{new_card_chet}'

    return result

