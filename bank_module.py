"""
Mock Bank API
"""
import utils


class BankAPI(object):
    def __init__(self):
        """Initializes the mock Bank API with empty sessions dictionary."""
        super()
        self.sessions = {}

    @staticmethod
    def card_lookup(card_number):
        """Returns True if `card_number` is in database."""
        return card_number in CARD_DATABASE

    def card_pin_lookup(self, card_number, pin):
        """Returns a tuple with its first element indicating pin's validity.

        :param card_number: card number to be looked up
        :param pin: the pin associated with the card_number
        :return: a Tuple (pin_valid, (session_id, session_key))
        """
        if card_number in CARD_DATABASE:
            session_id, session_key = None, None
            if pin == CARD_DATABASE[card_number]:
                session_id, session_key = utils.random_string(
                    26), utils.random_string(8)
                self.sessions[session_id] = session_key
            return pin == CARD_DATABASE[card_number], (session_id, session_key)
        raise KeyError('Card does not exist in the Bank\'s database')

    def list_accounts(self, session_id, session_key):
        """Lists the accounts linked with the card associated with the session.

        For the sake of simplicity, we have fixed the accounts for all cards
        """
        if session_id in self.sessions and self.sessions[
                session_id] == session_key:
            return ['Checkings 1', ' Checkings 2', 'Savings 1']
        raise Exception('Unauthorized attempt: session id/key is invalid')

    def view_balance(self, session_id, session_key, account):
        """Returns the balance of the account linked with the session.

        For the sake of simplicity, we have fixed the account balance
        """
        if session_id in self.sessions and self.sessions[
            session_id] == session_key and self._account_is_valid(session_id,
                                                                  session_key,
                                                                  account):
            return 10000
        raise Exception('Unauthorized attempt: session id/key/account' +
                        ' is invalid')

    def withdraw_amount(self, session_id, session_key, account, amount):
        """Returns a Tuple (success, new_balance) showing result of transaction.

        For the sake of simplicity, we have not implemented the Bank's
        withdrawal logic, just that it will return `True, new_balance` if
        successful and `False, old_balance` otherwise
        """
        if session_id in self.sessions and self.sessions[
            session_id] == session_key and self._account_is_valid(session_id,
                                                                  session_key,
                                                                  account):
            return True, 9000
        raise Exception('Unauthorized attempt: session id/key/account' +
                        ' is invalid')

    def deposit_amount(self, session_id, session_key, account, amount):
        """Returns a Tuple (success, new_balance) showing result of transaction.

        For the sake of simplicity, we have not implemented the Bank's
        deposit logic, just that it will return `True, new_balance` if
        successful and `False, old_balance` otherwise
        """
        if session_id in self.sessions and self.sessions[
            session_id] == session_key and self._account_is_valid(session_id,
                                                                  session_key,
                                                                  account):
            return True, 9000
        raise Exception('Unauthorized attempt: session id/key/account' +
                        ' is invalid')

    def delete_session(self, session_id, session_key):
        """Removes the session_id from the dictionary if the pair exists."""
        if self.sessions[session_id] == session_key:
            self.sessions.__delitem__(session_id)

    def _account_is_valid(self, session_id, session_key, account):
        """A mock private method to check existence of account for session."""
        return session_id in self.sessions and self.sessions[
            session_id] == session_key and True


# Mock Card-Pin Database that the mock Bank API uses
# Actual implementation varies and adds more secure storage
CARD_DATABASE = {"1234567890123456": "0000",
                 "2345678901234567": "0001",
                 "3456789012345678": "0002",
                 "1111111111111111": "0003"}
