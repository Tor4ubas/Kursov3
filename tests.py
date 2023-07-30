import utils
def test_format_date():
    assert utils.format_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert utils.format_date("2019-12-08T22:46:21.935582") == "08.12.2019"

def test_mask_card_number():
    assert utils.mask_card_number("Счет 72082042523231456215") == "Счет 7208 20** **** 6215"
    assert utils.mask_card_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"

def test_account_number():
    assert utils.account_number("Счет 72082042523231456215") == "** 6215"
    assert utils.account_number("Visa Classic 6831982476737658") == "** 7658"