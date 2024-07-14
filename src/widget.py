def get_mask_card_number(card_number: int) -> int:
    """Функция которая возвращает маску карты"""
    return card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]


def get_mask_account(card_number: int) -> int:
    """Функция которая маскирует номер счета"""
    return "**" + card_number[-4:]

def mask_account_card(numbers: str) -> str:
    if len(numbers.split()[1]) == 16:
        result = f'{numbers[:-16]}{get_mask_card_number(numbers.split()[1])}'


    #name_card = numbers[:-16]
    #account_ = numbers.split()[1]
    #new_masks_card = get_mask_card_number(numbers.split()[1])
    #print(account_)
    #print(name_card)
    #print(new_masks_card)




mask_account_card('Maestro 1596837868705199')
