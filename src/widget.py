def get_mask_card_number(number: int) -> int:
    """Функция которая возвращает маску карты"""
    return number[:4] + " " + number[4:6] + "** ****" + number[-4:]


def get_mask_account(number: int) -> int:
    """Функция которая маскирует номер счета"""
    return "**" + number[-4:]

def mask_account_card(numbers: str) -> str:
    if len(numbers.split()[1]) == 16:
        new_card = get_mask_card_number(numbers.split()[1])
        result = f'{numbers[:-16]}{get_mask_card_number(numbers.split()[1])}'


    elif len(numbers.split()[1]) == 20:
        result = f'{numbers[:-20]}'{get_mask_account(number.split()[1])}

    return result

    #name_card = numbers[:-16]
    #account_ = numbers.split()[1]
    #new_masks_card = get_mask_card_number(numbers.split()[1])
    #print(account_)
    #print(name_card)
    #print(new_masks_card)




mask_account_card('Maestro 1596837868705199')
