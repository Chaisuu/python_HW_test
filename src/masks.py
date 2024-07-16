def get_mask_card_number(card_number: int) -> int:
    """Функция которая возвращает маску карты"""
    return card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]


def get_mask_account(card_number: int) -> int:
    """Функция которая маскирует номер счета"""
    return "**" + card_number[-4:]
