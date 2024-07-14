def get_mask_card_number(card_number: int) -> int:
    """Функция которая возвращает маску карты"""
    return card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]


def get_mask_account(card_number: int) -> int:
    """Функция которая маскирует номер счета"""
    return "**" + card_number[-4:]

def mask_account_card(number:str) -> str
    account_ = mask_account_card.split(' ')[1]
    print(account_)


mask_account_card('Maestro 1596837868705199')
