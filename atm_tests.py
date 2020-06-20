import unittest
import atm_module


"""
The following class contains Unit tests for the class ATM in atm_module.py file.
"""


class ATMModuleTests(unittest.TestCase):
    def test_basic(self):
        atm = atm_module.ATM()
        atm.reset_session()
        self.assertTrue(atm.insert_card("1234567890123456"))
        self.assertFalse(atm.enter_pin("0042"))
        self.assertTrue(atm.enter_pin("0000"))
        self.assertListEqual(atm.list_accounts(), ['Checkings 1', ' Checkings 2', 'Savings 1'])
        self.assertTrue(atm.select_account(0))
        self.assertEqual(atm.view_balance(), 10000)
        self.assertTrue(atm.deposit_money(1000), 10000)
        self.assertTrue(atm.withdraw_money(3402), 10000)


if __name__ == '__main__':
    unittest.main()
