import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize ("card_number, expected_result",[
        (7000792289606361, '7000 79** **** 6361'),
        (7000792289606362, '7000 79** **** 6362'),
        (7000822289606363, '7000 82** **** 6363'),
        (7000822289606364, '7000 82** **** 6364'),
])

def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result



@pytest.mark.parametrize("card_number, result",[
    (73654108430135874305, '** 4305'),
    (73654108430135874306, '** 4306'),
    (73654108430135874307, '** 4307'),
    (73654108430135874308, '** 4308'),
])

def test_get_mask_account (card_number, result):
    assert get_mask_account(card_number) == result