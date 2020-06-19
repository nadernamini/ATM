import bank_module


class ATM(object):
    def __init__(self):
        super()
        self.bank_instance = bank_module.BankAPI()
        self._curr_card = None
        self._authorized = None

    def start_session(self):
        self._curr_card = None

    def end_session(self):
        self._curr_card = None

    def insert_card(self, card_number):
        if not self.bank_instance.card_lookup(card_number):
            raise KeyError('Card does not exist in the Bank\'s database')
        self._curr_card = card_number
        return True

    def enter_pin(self, pin_number):
        if self._curr_card is None:
            raise Exception("Card needs to be inserted before entering pin.")
        try:
            card_pin_lookup = self.bank_instance.card_pin_lookup(
                self._curr_card, pin_number)
        except KeyError:
            raise KeyError('Card does not exist in the Bank\'s database')
        if card_pin_lookup:
        return card_pin_lookup



