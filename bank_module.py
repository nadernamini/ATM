class BankAPI(object):
    def __init__(self):
        super()

    def card_lookup(self, card_number):
        return card_number in CARD_DATABASE

    def card_pin_lookup(self, card_number, pin):
        if card_number in CARD_DATABASE:

            return pin == CARD_DATABASE[card_number]
        raise KeyError('Card does not exist in the Bank\'s database')


CARD_DATABASE = {"1234567890123456": "0000",
                 "2345678901234567": "0001",
                 "3456789012345678": "0002",
                 "1111111111111111": "0003"}
