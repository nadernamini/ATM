"""
ATM Controller module
"""

import bank_module


class ATM(object):
    def __init__(self):
        super()
        self._bank_instance = bank_module.BankAPI()
        self._cash_bin = CashBin()
        self._curr_card = None
        self._authorized = None
        self._accounts_list = None
        self._account = None
        self._balance = None

    def reset_session(self):
        self._curr_card = None
        self._authorized = None
        self._accounts_list = None
        self._account = None
        self._balance = None

    def insert_card(self, card_number):
        """Initiates a session by ensuring card's validity and saving it."""
        if not self._bank_instance.card_lookup(card_number):
            raise KeyError('Card does not exist in the Bank\'s database')
        self._curr_card = card_number
        return True

    def enter_pin(self, pin_number):
        """Ensures that pin_number matches the pin on file for _curr_card."""
        if self._curr_card is None:
            raise Exception("Card needs to be inserted before entering pin.")
        try:
            card_pin_lookup = self._bank_instance.card_pin_lookup(
                self._curr_card, pin_number)
        except KeyError:
            raise KeyError('Card does not exist in the Bank\'s database')
        if card_pin_lookup[0]:
            self._authorized = card_pin_lookup[1]
        return card_pin_lookup[0]

    def list_accounts(self):
        """Returns a list of accounts associated with _curr_card."""
        if self._authorized is None:
            raise Exception('No authorized session is in progress')
        self._accounts_list = self._bank_instance.list_accounts(
            *self._authorized)
        return self._accounts_list

    def select_account(self, index):
        """Selects account at index-th position to continue (allows reuse)."""
        if index < 0 or index >= len(self._accounts_list):
            raise Exception(
                'Invalid index selected. Should be in range 0 (inclusive) and ' + str(
                    len(self._accounts_list)) + ' (exclusive).')
        self._account = self._accounts_list[index]
        return True

    def view_balance(self):
        """Returns the amount in dollars available in _account"""
        if self._authorized is None:
            raise Exception('No authorized session is in progress')
        if self._account is None:
            raise Exception('No account has been selected, yet')
        self._balance = self._bank_instance.view_balance(
            *(self._authorized + (self._account,)))
        return self._balance

    def withdraw_money(self, amount):
        """Calls Bank's API to withdraw from _account and returns status."""
        self.view_balance()
        if amount > self._balance:
            raise Exception('Unable to withdraw more money than the $' + str(
                self._balance) + ' available')
        success, self._balance = self._bank_instance.withdraw_amount(
            *(self._authorized + (self._account, amount)))
        if success:
            self._cash_bin.return_money(amount)
        return success

    def deposit_money(self, amount):
        """Calls Bank's API to deposit to _account and returns status.

        Please note that in reality, one could deposit both checks and cash.
        For brevity, we have only considered the case that the user is
        depositing cash.

        We have also modified ATM interaction by first asking the user the
        amount that they are trying to deposit and then verifying with the
        cash bin if it matches the cash input to the machine.

        Also, we have not considered the step where we prompt the user to input
        cash and have just skipped to the part where we inquire about the amount
        received.
        """
        self.view_balance()
        check, success = self._cash_bin.check_amount_received(amount), False
        if check:
            success, self._balance = self._bank_instance.deposit_amount(
                *(self._authorized + (self._account, amount)))
        return check and success


class CashBin(object):
    @staticmethod
    def return_money(amount):
        print('Returning $' + str(amount) + ' to user.')

    @staticmethod
    def check_amount_received(amount):
        return amount == 1000
