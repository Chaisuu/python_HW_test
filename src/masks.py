import logging

logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/masks.log', encoding="utf-8", mode="w")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str | int) -> str:
    card_number = str(card_number)
    """Функция которая возвращает маску карты"""
    logger.info("Mask for card numer created")
    return card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]


def get_mask_account(card_number: str | int) -> str:
    card_number = str(card_number)
    """Функция которая маскирует номер счета"""
    logger.info("Mask for account created")
    return "**" + " " + card_number[-4:]
